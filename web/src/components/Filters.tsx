'use client';

export interface FilterState {
  auth: string;
  https: string;
  cors: string;
}

interface FiltersProps {
  filters: FilterState;
  onChange: (filters: FilterState) => void;
}

export default function Filters({ filters, onChange }: FiltersProps) {
  const updateFilter = (key: keyof FilterState, value: string) => {
    onChange({ ...filters, [key]: value });
  };

  const selectStyle = {
    backgroundColor: 'var(--card-bg)',
    borderColor: 'var(--card-border)',
    color: 'var(--foreground)',
  };

  return (
    <div className="flex flex-wrap gap-3">
      <select
        value={filters.auth}
        onChange={(e) => updateFilter('auth', e.target.value)}
        className="px-4 py-2 rounded-lg border outline-none cursor-pointer transition-colors text-sm"
        style={selectStyle}
      >
        <option value="">All Auth Types</option>
        <option value="No">No Auth</option>
        <option value="apiKey">API Key</option>
        <option value="OAuth">OAuth</option>
      </select>

      <select
        value={filters.https}
        onChange={(e) => updateFilter('https', e.target.value)}
        className="px-4 py-2 rounded-lg border outline-none cursor-pointer transition-colors text-sm"
        style={selectStyle}
      >
        <option value="">Any HTTPS</option>
        <option value="yes">HTTPS Only</option>
        <option value="no">HTTP Only</option>
      </select>

      <select
        value={filters.cors}
        onChange={(e) => updateFilter('cors', e.target.value)}
        className="px-4 py-2 rounded-lg border outline-none cursor-pointer transition-colors text-sm"
        style={selectStyle}
      >
        <option value="">Any CORS</option>
        <option value="Yes">CORS Enabled</option>
        <option value="No">No CORS</option>
        <option value="Unknown">Unknown</option>
      </select>

      {(filters.auth || filters.https || filters.cors) && (
        <button
          onClick={() => onChange({ auth: '', https: '', cors: '' })}
          className="px-4 py-2 rounded-lg text-sm font-medium transition-colors"
          style={{
            backgroundColor: 'var(--accent)',
            color: 'white'
          }}
        >
          Clear Filters
        </button>
      )}
    </div>
  );
}
