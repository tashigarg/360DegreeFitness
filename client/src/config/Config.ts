// Auth server (Express)
// export const BASE_URL = "http://127.0.0.1:5050";
export const BASE_URL = process.env.REACT_APP_BASE_URL || "http://localhost:5050" || "http://127.0.0.1:5050";

// AI server (FastAPI)
// export const AI_BASE_URL = "http://127.0.0.1:8000";
export const AI_BASE_URL = process.env.REACT_APP_AI_BASE_URL || "http://localhost:8000" || "http://127.0.0.1:8000";

// API paths
export const API_PATHS = {
    AUTH: `${BASE_URL}/api/auth`,
    CHAT: `${AI_BASE_URL}/v1/360_degree_fitness`,
    PROFILE: `${BASE_URL}/api/profile`
};

export const getHeaders = (userData: { token: string }) => ({
    headers: {
        "x-auth-token": userData.token
    }
});
