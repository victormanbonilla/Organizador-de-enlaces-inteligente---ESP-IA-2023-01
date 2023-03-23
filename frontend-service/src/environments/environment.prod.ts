import axios from "axios";
import { useAuthStore } from "../modules/auth/composables/useAuthStore";

const http = axios.create({
    baseURL: import.meta.env.VITE_BACKEND_URL,
});

http.interceptors.request.use(config => {
    const { user } = useAuthStore();
    const rawUser = { ...user.value };
    
    if (rawUser.token) {
        config.headers['token'] = rawUser.token;
    }
    return config;
});

export { http };
