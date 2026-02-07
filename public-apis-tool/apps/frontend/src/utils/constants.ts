export const HOST = import.meta.env.VITE_SERVER_URL;

export const APIS_ROUTE = `/apis`;

export const AUTH_ROUTES = `/auth`;
export const GITHUB_AUTH_ROUTE = `${AUTH_ROUTES}/github`;

export const USER_ROUTES = `/user`;
export const GET_ME = `${USER_ROUTES}/me`;
export const LOGOUT_ROUTE = `${USER_ROUTES}/logout`;
