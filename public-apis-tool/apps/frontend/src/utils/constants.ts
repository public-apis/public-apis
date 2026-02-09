export const HOST = import.meta.env.VITE_SERVER_URL;

export const APIS_ROUTE = `/apis`;
export const GET_CATEGORIES = `${APIS_ROUTE}/get-categories`;

export const AUTH_ROUTES = `/auth`;
export const GITHUB_AUTH_ROUTE = `${HOST}${AUTH_ROUTES}/github`;

export const USER_ROUTES = `/user`;
export const GET_ME = `${USER_ROUTES}/me`;
export const LOGOUT_ROUTE = `${USER_ROUTES}/logout`;

export const GITHUB_ROUTES = "/github";
export const ADD_API_ROUTE = `${GITHUB_ROUTES}/add-api`;
