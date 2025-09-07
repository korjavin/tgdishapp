# Family Dish Duty Tracker

A Telegram web app to track and delegate dish duties for the family. This project is configured to run securely in containers using Docker or Podman, with automatic HTTPS provided by a Caddy reverse proxy.

## Features

-   Calendar view of dish duties.
-   Admin can delegate duties to registered users.
-   Users can see their designated duties.
-   Users can self-delegate to a free day in the future.
-   Archive of past duties.
-   Secure by default with HTTPS.

## Prerequisites

-   Docker or Podman with `docker-compose` or `podman-compose`.
-   A Telegram Bot Token from [@BotFather](https://t.me/BotFather).
-   A domain name (for production) or `localhost` (for development).

---

## Development Setup (with HTTPS)

This setup runs the application from local source code, with live-reloading for the backend. Caddy is included to provide automatic HTTPS on `localhost`.

1.  **Clone the Repository:**
    ```bash
    git clone <repository-url>
    cd <repository-name>
    ```

2.  **Configure Environment:**
    Copy `.env.example` to `.env` and fill in the variables.
    ```bash
    cp .env.example .env
    ```
    -   `TELEGRAM_BOT_TOKEN`: Your Telegram bot token.
    -   `ADMIN_USER_ID`: Your Telegram user ID for admin rights.
    -   `DOMAIN`: For local development, set this to `localhost`.
    -   `DATABASE_URL`: Defaults to `sqlite:///db/duties.db`. The database will be stored in a persistent Docker volume.
    -   `IMAGE_NAME`: Not used in development.

3.  **Run the Application:**
    -   **Using Docker:**
        ```bash
        docker-compose up --build
        ```
    -   **Using Podman:**
        ```bash
        podman-compose up --build
        ```
    The first time you run this, Caddy will generate and install a local CA and SSL certificate. You may be prompted for your `sudo` password.

4.  **Access the Application:**
    Open your browser and navigate to `https://localhost`. You should see the application running with a valid SSL certificate.

---

## Production Deployment

This setup pulls a pre-built container image from a registry and runs it. It is designed for a production server with a public domain name.

1.  **CI/CD:**
    The GitHub Actions workflow in this repository automatically builds and pushes the container image to the GitHub Container Registry (`ghcr.io`) on every push to the `main` branch.

2.  **Server Setup:**
    -   Clone this repository on your production server.
    -   Ensure Docker or Podman is installed.

3.  **Configure Environment:**
    Create an `.env` file and fill in the production values:
    -   `TELEGRAM_BOT_TOKEN`: Your production Telegram bot token.
    -   `ADMIN_USER_ID`: The production admin's Telegram user ID.
    -   `DOMAIN`: Your public domain name (e.g., `dishes.example.com`).
    -   `DATABASE_URL`: It's highly recommended to use a robust database like PostgreSQL in production.
    -   `IMAGE_NAME`: The full path to the container image, e.g., `ghcr.io/your-org/your-repo:latest`.

4.  **Run the Application:**
    -   **Using Docker:**
        ```bash
        docker-compose -f docker-compose.prod.yml up -d
        ```
    -   **Using Podman:**
        ```bash
        podman-compose -f docker-compose.prod.yml up -d
        ```
    Caddy will automatically obtain a trusted SSL certificate from Let's Encrypt for your domain.

5.  **Telegram Integration:**
    -   In Telegram, talk to `@BotFather`.
    -   Set your bot's Web App URL to your public domain: `https://<your-domain>`.

---

## Running as a Non-Privileged User

Binding to privileged ports (80, 443) typically requires root. Here’s how to handle it without running Docker or Podman as root.

### For Docker

You can grant the Docker daemon the capability to bind to low-numbered ports.

1.  **Find the Docker proxy path:**
    ```bash
    ps aux | grep docker-proxy
    ```
    This will show you the path to the `docker-proxy` binary.

2.  **Grant capabilities:**
    ```bash
    sudo setcap cap_net_bind_service=+ep /path/to/your/docker-proxy
    ```

### For Podman

Podman runs rootless by default. You can allow rootless users to bind to privileged ports via a system configuration.

1.  **Edit `sysctl.conf`:**
    ```bash
    sudo nano /etc/sysctl.conf
    ```

2.  **Add the following line:**
    ```
    net.ipv4.ip_unprivileged_port_start=80
    ```

3.  **Apply the changes:**
    ```bash
    sudo sysctl --system
    ```
This allows any user to bind to ports 80 and above.
