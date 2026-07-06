'use strict';

// Zero-dependency client-side search/filter for the glibc API index.
// Loads ./data/index.json (produced by scripts/build_index.py) and renders a
// filterable table. No framework, no build step.

const state = {
  data: { modules: [], functions: [] },
};

function uniq(arr) {
  return Array.from(new Set(arr)).sort();
}

function populateSelect(id, values) {
  const sel = document.getElementById(id);
  values.forEach((v) => {
    const opt = document.createElement('option');
    opt.value = v;
    opt.textContent = v;
    sel.appendChild(opt);
  });
}

function escapeHtml(s) {
  return String(s)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

function applyFilters() {
  const q = document.getElementById('search').value.trim().toLowerCase();
  const cat = document.getElementById('filter-category').value;
  const std = document.getElementById('filter-standard').value;
  const hdr = document.getElementById('filter-header').value;
  const mts = document.getElementById('filter-mtsafe').value;

  const results = state.data.functions.filter((f) => {
    if (cat && f.category !== cat) return false;
    if (std && f.standard !== std) return false;
    if (hdr && f.header !== hdr) return false;
    if (mts && f.mtSafe !== mts) return false;
    if (q) {
      const hay = (f.function + ' ' + f.description).toLowerCase();
      if (hay.indexOf(q) === -1) return false;
    }
    return true;
  });

  render(results);
}

function render(results) {
  const tbody = document.querySelector('#results tbody');
  tbody.innerHTML = '';

  if (results.length === 0) {
    const tr = document.createElement('tr');
    tr.innerHTML = '<td colspan="6" class="empty">No functions match your filters.</td>';
    tbody.appendChild(tr);
  } else {
    results.forEach((f) => {
      const tr = document.createElement('tr');
      const cells = [
        `<td><a href="${escapeHtml(f.link)}" target="_blank" rel="noopener">${escapeHtml(f.function)}</a></td>`,
        `<td><code>${escapeHtml(f.header)}</code></td>`,
        `<td>${escapeHtml(f.description)}</td>`,
        `<td>${escapeHtml(f.standard)}</td>`,
        `<td>${escapeHtml(f.mtSafe)}</td>`,
        `<td>${escapeHtml(f.category)}</td>`,
      ];
      tr.innerHTML = cells.join('');
      tbody.appendChild(tr);
    });
  }

  document.getElementById('count').textContent =
    results.length + ' / ' + state.data.functions.length + ' functions';
}

async function init() {
  try {
    const resp = await fetch('./data/index.json');
    if (!resp.ok) throw new Error('Failed to load index.json: HTTP ' + resp.status);
    state.data = await resp.json();
  } catch (e) {
    document.getElementById('count').textContent = 'Error: ' + e.message;
    return;
  }

  populateSelect('filter-category', uniq(state.data.functions.map((f) => f.category)));
  populateSelect('filter-standard', uniq(state.data.functions.map((f) => f.standard)));
  populateSelect('filter-header', uniq(state.data.functions.map((f) => f.header)));
  populateSelect('filter-mtsafe', uniq(state.data.functions.map((f) => f.mtSafe)));

  ['search', 'filter-category', 'filter-standard', 'filter-header', 'filter-mtsafe']
    .forEach((id) => document.getElementById(id).addEventListener('input', applyFilters));

  applyFilters();
}

document.addEventListener('DOMContentLoaded', init);
