'use client';

import { API } from '@/utils/types';

interface APICardProps {
  api: API;
}

export default function APICard({ api }: APICardProps) {
  const getAuthBadge = () => {
    if (api.auth === 'No') return null;
    return (
      <span className="badge badge-auth">
        {api.auth === 'apiKey' ? 'API Key' : api.auth}
      </span>
    );
  };

  const getHttpsBadge = () => (
    <span className={`badge ${api.https ? 'badge-https-yes' : 'badge-https-no'}`}>
      {api.https ? 'HTTPS' : 'HTTP'}
    </span>
  );

  const getCorsBadge = () => {
    const corsClass = api.cors === 'Yes'
      ? 'badge-cors-yes'
      : api.cors === 'No'
        ? 'badge-cors-no'
        : 'badge-cors-unknown';
    return (
      <span className={`badge ${corsClass}`}>
        CORS: {api.cors}
      </span>
    );
  };

  return (
    <a
      href={api.url}
      target="_blank"
      rel="noopener noreferrer"
      className="api-card block p-5 rounded-xl border transition-theme"
      style={{
        backgroundColor: 'var(--card-bg)',
        borderColor: 'var(--card-border)',
      }}
    >
      <div className="flex items-start justify-between gap-3 mb-3">
        <h3 className="font-semibold text-lg leading-tight" style={{ color: 'var(--foreground)' }}>
          {api.name}
        </h3>
        <svg
          className="w-4 h-4 flex-shrink-0 mt-1"
          style={{ color: 'var(--muted)' }}
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2}
            d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
        </svg>
      </div>

      <p className="text-sm mb-4 line-clamp-2" style={{ color: 'var(--muted)' }}>
        {api.description}
      </p>

      <div className="flex flex-wrap gap-2">
        {getAuthBadge()}
        {getHttpsBadge()}
        {getCorsBadge()}
      </div>
    </a>
  );
}
