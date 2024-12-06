import React from 'react';

interface StatusMessageProps {
  type: 'success' | 'error' | null;
  message: string;
}

export const StatusMessage: React.FC<StatusMessageProps> = ({ type, message }) => {
  if (!type || !message) return null;

  return (
    <div
      className={`mt-4 p-4 rounded-md ${
        type === 'success'
          ? 'bg-green-50 text-green-800'
          : 'bg-red-50 text-red-800'
      }`}
    >
      {message}
    </div>
  );
};