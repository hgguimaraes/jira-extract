import { parse, isValid, format } from 'date-fns';

export const formatDateToJira = (dateStr: string): string => {
  const date = parse(dateStr, 'dd/MM/yyyy', new Date());
  return format(date, 'yyyy-MM-dd');
};

export const isValidDate = (dateStr: string): boolean => {
  if (!/^\d{2}\/\d{2}\/\d{4}$/.test(dateStr)) {
    return false;
  }
  
  const date = parse(dateStr, 'dd/MM/yyyy', new Date());
  return isValid(date);
};