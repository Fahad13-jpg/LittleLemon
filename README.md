Little Lemon API

Please test the following API endpoints.

## Public Endpoints

GET    /restaurant/menu/
GET    /restaurant/menu/[int:pk](int:pk)/

## Protected Endpoints

POST   /restaurant/menu/
PUT    /restaurant/menu/[int:pk](int:pk)/
DELETE /restaurant/menu/[int:pk](int:pk)/

GET    /restaurant/booking/tables/
POST   /restaurant/booking/tables/
PUT    /restaurant/booking/tables/[int:pk](int:pk)/
DELETE /restaurant/booking/tables/[int:pk](int:pk)/

## User Registration & Authentication

POST   /auth/users/
POST   /auth/token/login/
POST   /auth/token/logout/
POST   /auth/jwt/verify/

