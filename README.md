# Family Dish Duty Tracker

A Telegram web app to track and delegate dish duties for the family.

## Features

- Calendar view of dish duties.
- Admin can delegate duties to registered users.
- Users can see their designated duties.
- Users can self-delegate to a free day in the future.
- Archive of past duties.

## Development Setup

### Prerequisites

- Docker or Podman
- A Telegram Bot Token from [@BotFather](https://t.me/BotFather)

### Instructions

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-name>
    ```

2.  **Create an environment file:**
    Copy the `.env.example` file to `.env` and fill in the required values.
    ```bash
    cp .env.example .env
    ```
    - `TELEGRAM_BOT_TOKEN`: Your Telegram bot token.
    - `ADMIN_USER_ID`: Your Telegram user ID. This user will have admin privileges.
    - `DOMAIN`: The domain name for your web app (e.g., `localhost` for local development).

3.  **Run the application:**
    - **Using Docker:**
      ```bash
      docker-compose up --build
      ```
    - **Using Podman:**
      ```bash
      podman-compose up --build
      ```
      If you encounter issues with port binding, you may need to allow non-privileged users to bind to privileged ports. For Podman, you can use:
      ```bash
      sudo sysctl net.ipv4.ip_unprivileged_port_start=80
      ```

4.  **Access the application:**
    Open your browser and navigate to `http://{$DOMAIN}` (e.g., `http://localhost`).

## Production Deployment

### Prerequisites

- A server with Docker or Podman installed.
- A registered domain name pointing to your server's IP address.
- A container image pushed to a registry (e.g., GitHub Container Registry).

### Instructions

1.  **Push the Docker image to a registry:**
    The CI/CD workflow in this repository is configured to build and push the image to `ghcr.io` automatically on pushes to the `main` branch.

2.  **Prepare the server:**
    - Clone the repository to your server.
    - Create the `.env` file as described in the development setup. Make sure to set the `DOMAIN` to your registered domain name.

3.  **Run the application:**
    - **Using Docker:**
      ```bash
      docker-compose -f docker-compose.prod.yml up -d
      ```
    - **Using Podman:**
      ```bash
      podman-compose -f docker-compose.prod.yml up -d
      ```

4.  **Access the application:**
    The application will be available at `https://{$DOMAIN}` with HTTPS automatically configured by Caddy.

## Deploy to Render

You can deploy this application to Render by clicking the button below.

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

Alternatively, you can manually deploy by following these steps:

1.  **Fork this repository.**
2.  **Create a new "Blueprint" service on Render.**
3.  **Connect your forked repository.**
4.  **Render will automatically detect the `render.yaml` file and configure the services.**
5.  **Add the required environment variables in the Render dashboard:**
    - `TELEGRAM_BOT_TOKEN`: Your Telegram bot token.
    - `ADMIN_USER_ID`: Your Telegram user ID.

The `DATABASE_URL` and `DOMAIN` variables will be automatically set by Render.

## Telegram Integration

To integrate with Telegram, you need to:
1.  Create a bot with [@BotFather](https://t.me/BotFather).
2.  Set the bot's web app URL to your application's URL.
3.  The application will use the user's Telegram ID for authentication.
