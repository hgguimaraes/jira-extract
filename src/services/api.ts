import axios from 'axios';
import { API_CONFIG } from '../config/api';

export const api = axios.create({
  baseURL: API_CONFIG.baseUrl,
  headers: {
    'Content-Type': 'application/json',
  },
});

api.interceptors.response.use(
  response => response,
  error => {
    if (error.code === 'ECONNREFUSED') {
      throw new Error('Unable to connect to the server. Please ensure the API is running.');
    }
    
    if (!error.response) {
      throw new Error('Network error. Please check your internet connection.');
    }
    
    const errorMessage = error.response?.data?.error || error.message;
    throw new Error(errorMessage);
  }
);