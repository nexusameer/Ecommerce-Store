# Ecommerce-Store

This project is a fully functional E-commerce web application developed as a final year university project. It allows users to browse products, filter by categories and brands, add items to a shopping cart, and manage their orders.

## Features

- User authentication and registration
- Product listing with categories and brands
- Product detail pages
- Shopping cart functionality
- Price range filter
- Checkout process (basic)
- Responsive UI with templates for homepage, shop, product, and blog pages

## Technologies Used

- **Backend:** Django 3.1.13 (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite3 (default with Django)
- **Other:** Bootstrap (for responsive design), Font Awesome (icons)

## Directory Structure

- `Eshop/` – Django project settings
- `app/`, `cart/` – Django apps for main store functionality and cart
- `templates/` – HTML templates for various pages
- `static/` – CSS, JS, images for the frontend

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/nexusameer/Ecommerce-Store.git
   cd Ecommerce-Store
   ```

2. **Create a virtual environment and activate it:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install django==3.1.13
   ```

4. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

6. **Access the app:**
   Open your browser and navigate to `http://127.0.0.1:8000/`

## Project Structure and Main Files

- `manage.py` – Django project management script
- `Eshop/settings.py` – Django settings (configured for SQLite3)
- `templates/` – Contains `index.html`, `shop.html`, `product.html`, etc.
- `static/` – Contains CSS (`price-range.css`), JS (`gmaps.js`, `price-range.js`), images

## Contribution

As this is a university project, contributions are currently not accepted. For any queries or suggestions, feel free to open an issue.

## License

No license specified.

## Author

- [nexusameer](https://github.com/nexusameer)

---

*This project was developed as a final year university project to demonstrate a complete e-commerce workflow using Django.*

[Explore the code on GitHub](https://github.com/nexusameer/Ecommerce-Store)
