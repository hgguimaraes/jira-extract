import React, { useState } from 'react';
import { FileText } from 'lucide-react';
import { DateInput } from './components/DateInput';
import { StatusMessage } from './components/StatusMessage';
import { ExtractButton } from './components/ExtractButton';
import { extractJiraComments } from './services/jiraService';
import { formatDateToJira, isValidDate } from './utils/dateUtils';

function App() {
  const [startDate, setStartDate] = useState('');
  const [endDate, setEndDate] = useState('');
  const [status, setStatus] = useState<{
    type: 'success' | 'error' | null;
    message: string;
  }>({ type: null, message: '' });
  const [isLoading, setIsLoading] = useState(false);

  const validateDates = (): string[] => {
    const errors: string[] = [];
    
    if (!startDate) errors.push('Start date is required');
    if (!endDate) errors.push('End date is required');
    
    if (startDate && !isValidDate(startDate)) {
      errors.push('Invalid start date format');
    }
    
    if (endDate && !isValidDate(endDate)) {
      errors.push('Invalid end date format');
    }
    
    return errors;
  };

  const handleExtract = async () => {
    const errors = validateDates();
    if (errors.length > 0) {
      setStatus({
        type: 'error',
        message: errors.join('. '),
      });
      return;
    }

    setIsLoading(true);
    setStatus({ type: null, message: '' });

    try {
      const result = await extractJiraComments({
        startDate: formatDateToJira(startDate),
        endDate: formatDateToJira(endDate),
      });

      if (result.success) {
        setStatus({
          type: 'success',
          message: 'Data exported successfully to jira_filtered_comments1.csv',
        });
      } else {
        setStatus({
          type: 'error',
          message: result.error || 'Failed to extract comments',
        });
      }
    } catch (error) {
      setStatus({
        type: 'error',
        message: error instanceof Error ? error.message : 'An unknown error occurred',
      });
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-md mx-auto bg-white rounded-lg shadow-md p-6">
        <div className="flex items-center justify-center mb-8">
          <FileText className="h-12 w-12 text-blue-500" />
          <h1 className="ml-3 text-2xl font-bold text-gray-900">
            Jira Comments Extractor
          </h1>
        </div>

        <div className="space-y-6">
          <div className="grid grid-cols-2 gap-4">
            <DateInput
              label="Start Date"
              value={startDate}
              onChange={setStartDate}
            />
            <DateInput
              label="End Date"
              value={endDate}
              onChange={setEndDate}
            />
          </div>

          <ExtractButton
            onClick={handleExtract}
            isLoading={isLoading}
          />

          <StatusMessage
            type={status.type}
            message={status.message}
          />
        </div>
      </div>
    </div>
  );
}

export default App;