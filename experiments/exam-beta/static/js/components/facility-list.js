const FacilityList = {
    template: `
        <div>
            <h2 class="mb-4">{{ $t('facility.search') }}</h2>
            <div class="row mb-4">
                <div class="col-md-6 mb-2">
                    <input v-model="search.q" class="form-control" :placeholder="$t('facility.search')" @input="debounceSearch">
                </div>
                <div class="col-md-2 mb-2">
                    <select v-model="search.type" class="form-select" @change="fetchFacilities">
                        <option value="">{{ $t('facility.all') }}</option>
                        <option value="gym">{{ $t('facility.gym') }}</option>
                        <option value="meeting_room">{{ $t('facility.meeting_room') }}</option>
                        <option value="pool">{{ $t('facility.pool') }}</option>
                    </select>
                </div>
                <div class="col-md-2 mb-2">
                    <input v-model.number="search.capacity" class="form-control" :placeholder="$t('facility.capacity')" @input="fetchFacilities">
                </div>
                <div class="col-md-2 mb-2">
                    <input v-model.number="search.max_price" class="form-control" :placeholder="$t('facility.price')" @input="fetchFacilities">
                </div>
            </div>

            <div v-if="loading" class="text-center py-4">
                <div class="spinner-border text-primary" role="status"></div>
            </div>

            <div v-else-if="facilities.length === 0" class="alert alert-info">
                {{ $t('facility.no_results') }}
            </div>

            <div v-else class="row">
                <div v-for="f in facilities" :key="f.id" class="col-md-6 col-lg-4 mb-4">
                    <div class="card h-100">
                        <div class="card-body">
                            <h5 class="card-title">{{ f.name }}</h5>
                            <p class="card-text text-muted">{{ f.address }}</p>
                            <span class="badge bg-secondary me-1">{{ typeLabel(f.type) }}</span>
                            <p class="mt-2 mb-1"><strong>{{ $t('facility.capacity') }}:</strong> {{ f.capacity }}{{ $t('reservation.person') }}</p>
                            <p class="mb-2"><strong>{{ $t('facility.price') }}:</strong> {{ f.price_per_hour.toLocaleString() }}{{ $t('facility.per_hour') }}</p>
                            <a href="#" class="btn btn-primary" @click="$root.navigate('/facility?id=' + f.id)">{{ $t('facility.detail') }}</a>
                            <a href="#" class="btn btn-outline-primary ms-2" @click="$root.navigate('/reserve?id=' + f.id)">{{ $t('facility.reserve') }}</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    `,
    data() {
        return {
            search: { q: '', type: '', capacity: null, max_price: null },
            facilities: [],
            loading: false,
            debounceTimer: null
        };
    },
    methods: {
        typeLabel(type) {
            const labels = { gym: this.$t('facility.gym'), meeting_room: this.$t('facility.meeting_room'), pool: this.$t('facility.pool') };
            return labels[type] || type;
        },
        debounceSearch() {
            clearTimeout(this.debounceTimer);
            this.debounceTimer = setTimeout(() => this.fetchFacilities(), 300);
        },
        async fetchFacilities() {
            this.loading = true;
            try {
                const params = new URLSearchParams();
                if (this.search.q) params.set('q', this.search.q);
                if (this.search.type) params.set('type', this.search.type);
                if (this.search.capacity) params.set('capacity', this.search.capacity);
                if (this.search.max_price) params.set('max_price', this.search.max_price);
                params.set('lang', i18n.global.locale);
                const result = await apiFetch('/api/facilities?' + params.toString());
                this.facilities = result.items;
            } catch (e) {
                console.error(e);
            } finally {
                this.loading = false;
            }
        }
    },
    mounted() {
        this.fetchFacilities();
    }
};
