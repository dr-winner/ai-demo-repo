import axios, { AxiosError } from 'axios';

const API_URL = process.env.EXPO_PUBLIC_API_BASE_URL || 'http://localhost:8000';

export const apiClient = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

apiClient.interceptors.response.use(
  (response) => response.data,
  (error: AxiosError) => {
    // Handle global API errors here (e.g., logging, toast notifications)
    console.error('API Error:', error.response?.data || error.message);
    return Promise.reject(error);
  }
);
