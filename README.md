# Family Dish Duty Tracker

A Telegram web app to track and delegate dish duties for the family. This project is configured to be securely exposed via Traefik, a modern reverse proxy.

## Features

-   Calendar view of dish duties.
-   Admin can delegate duties to registered users.
-   Users can see their designated duties.
-   Users can self-delegate to a free day in the future.
-   Archive of past duties.

## Prerequisites

-   An existing Traefik v2 instance running in Docker.
-   The Traefik instance must be connected to a Docker network (e.g., `proxy`).
-   Docker or Podman with `docker-compose` or `podman-compose`.
-   A Telegram Bot Token from [@BotFather](https://t.me/BotFather).
-   A domain name (for production) or `localhost` (for development).

---

## Development Setup

This setup runs the application from local source code, with live-reloading for the backend. It's designed to be automatically discovered by your existing Traefik container.

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
    -   `DOMAIN`: The hostname Traefik should use. For local development, you might use `app.localhost` and modify your `/etc/hosts` file accordingly.
    -   `DATABASE_URL`: Defaults to `sqlite:///db/duties.db`. The database will be stored in a persistent Docker volume.
    -   `TRAEFIK_NETWORK`: The name of your external Traefik network (e.g., `proxy`).

3.  **Run the Application:**
    -   **Using Docker:**
        ```bash
        docker-compose up --build
        ```
    -   **Using Podman:**
        ```bash
        podman-compose up --build
        ```
    Traefik will detect the running container via its labels and automatically configure routing and HTTPS.

4.  **Access the Application:**
    Open your browser and navigate to `https://<your-domain>`.

---

## Production Deployment

This setup pulls a pre-built container image from a registry and runs it.

1.  **CI/CD:**
    The GitHub Actions workflow in this repository automatically builds and pushes the container image to the GitHub Container Registry (`ghcr.io`) on every push to the `main` branch.

2.  **Server Setup:**
    -   Clone this repository on your production server.
    -   Ensure your Traefik instance is running and connected to the external network.

3.  **Configure Environment:**
    Create an `.env` file and fill in the production values:
    -   `TELEGRAM_BOT_TOKEN`: Your production Telegram bot token.
    -   `ADMIN_USER_ID`: The production admin's Telegram user ID.
    -   `DOMAIN`: Your public domain name (e.g., `dishes.example.com`).
    -   `DATABASE_URL`: It's highly recommended to use a robust database like PostgreSQL in production.
    -   `IMAGE_NAME`: The full path to the container image from the registry, e.g., `ghcr.io/your-org/your-repo:latest`.
    -   `TRAEFIK_NETWORK`: The name of your external Traefik network.

4.  **Run the Application:**
    -   **Using Docker:**
        ```bash
        docker-compose -f docker-compose.prod.yml up -d
        ```
    -   **Using Podman:**
        ```bash
        podman-compose -f docker-compose.prod.yml up -d
        ```
    Traefik will handle obtaining and renewing the SSL certificate for your domain.

5.  **Telegram Integration:**
    -   In Telegram, talk to `@BotFather`.
    -   Set your bot's Web App URL to your public domain: `https://<your-domain>`.
