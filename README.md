# Asyncio Deck Draw

This repository contains a Python script that demonstrates how to perform fast concurrent HTTP requests using the `asyncio` and `aiohttp` libraries. The script draws multiple cards concurrently from the Deck of Cards API, showcasing efficient asynchronous programming.

## Features
- Utilizes `asyncio` and `aiohttp` to perform up to 105 concurrent card draw requests.
- Reuses a single session for efficiency.
- Implements basic error handling and concurrency control.

## Usage
1. **Clone the Repository:**
    ```bash
    git clone https://github.com/yourusername/async-draw-cards.git
    cd async-draw-cards
    ```

2. **Install Dependencies:**
    ```bash
    pip install aiohttp
    ```

3. **Run the Script:**
    ```bash
    python draw_cards.py
    ```

## Script Description
The script draws cards asynchronously using `aiohttp` for HTTP requests and `asyncio` for concurrency. It uses a `ClientSession` to manage connections and a TCP connector to limit concurrent connections for efficiency.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
