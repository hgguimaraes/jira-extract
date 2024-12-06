import { api } from './api';
import { API_CONFIG } from '../config/api';
import { ApiResponse, DateRange } from '../types/api';

export const extractJiraComments = async (dateRange: DateRange): Promise<ApiResponse> => {
  try {
    const response = await api.post(API_CONFIG.endpoints.extractComments, dateRange);
    return { success: true, data: response.data };
  } catch (error) {
    if (error instanceof Error) {
      return { 
        success: false, 
        error: error.message 
      };
    }
    return { 
      success: false, 
      error: 'An unexpected error occurred' 
    };
  }
};