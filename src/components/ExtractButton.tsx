import React from 'react';
import { Calendar, Download } from 'lucide-react';

interface ExtractButtonProps {
  onClick: () => void;
  isLoading: boolean;
}

export const ExtractButton: React.FC<ExtractButtonProps> = ({ onClick, isLoading }) => {
  return (
    <button
      onClick={onClick}
      disabled={isLoading}
      className={`w-full flex items-center justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white ${
        isLoading
          ? 'bg-blue-400 cursor-not-allowed'
          : 'bg-blue-600 hover:bg-blue-700'
      }`}
    >
      {isLoading ? (
        <>
          <Calendar className="animate-spin -ml-1 mr-2 h-4 w-4" />
          Processing...
        </>
      ) : (
        <>
          <Download className="-ml-1 mr-2 h-4 w-4" />
          Extract Comments
        </>
      )}
    </button>
  );
};