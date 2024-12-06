export interface ApiResponse<T = any> {
  success: boolean;
  data?: T;
  error?: string;
}

export interface DateRange {
  startDate: string;
  endDate: string;
}

export interface JiraComment {
  key: string;
  title: string;
  date: string;
  comment: string;
}