const store = Vue.reactive({
    user: null,
    facilities: [],
    currentFacility: null,
    reservations: [],
    currentReservation: null,
    searchQuery: {
        q: '',
        type: '',
        min_price: null,
        max_price: null,
        capacity: null
    }
});

async function apiFetch(url, options = {}) {
    const config = {
        headers: { 'Content-Type': 'application/json' },
        ...options
    };
    const response = await fetch(url, config);
    if (!response.ok) {
        const error = await response.json();
        throw error;
    }
    return response.json();
}
