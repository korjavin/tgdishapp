# Family Dish Duty Tracker

A Telegram web app to track and delegate dish duties for the family.

## Features

- Calendar view of dish duties.
- Admin can delegate duties to registered users.
- Users can see their designated duties.
- Users can self-delegate to a free day in the a future.
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

3.  **Run the application:**
    - **Using Docker:**
      ```bash
      docker-compose up --build
      ```
    - **Using Podman:**
      ```bash
      podman-compose up --build
      ```

4.  **Access the application:**
    Open your browser and navigate to `http://localhost:8000`.

## Production Deployment

### Prerequisites

- A server with Docker or Podman installed.
- A reverse proxy (like Traefik, Nginx, or Caddy) to handle SSL termination.
- A registered domain name pointing to your server's IP address.
- A container image pushed to a registry (e.g., GitHub Container Registry).

### Instructions

1.  **Push the Docker image to a registry:**
    The CI/CD workflow in this repository is configured to build and push the image to `ghcr.io` automatically on pushes to the `main` branch.

2.  **Prepare the server:**
    - Clone the repository to your server.
    - Create the `.env` file as described in the development setup.

3.  **Run the application:**
    - **Using Docker:**
      ```bash
      docker-compose -f docker-compose.prod.yml up -d
      ```
    - **Using Podman:**
      ```bash
      podman-compose -f docker-compose.prod.yml up -d
      ```

4.  **Configure your reverse proxy:**
    Configure your external reverse proxy (e.g., Traefik) to point to the application running on port 8000.

## Telegram Integration

To integrate with Telegram, you need to:
1.  Create a bot with [@BotFather](https://t.me/BotFather).
2.  Set the bot's web app URL to your application's public URL (handled by your reverse proxy).
3.  The application will use the user's Telegram ID for authentication.
