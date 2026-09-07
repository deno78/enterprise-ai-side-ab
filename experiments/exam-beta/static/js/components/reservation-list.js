const ReservationList = {
    template: `
        <div>
            <h2 class="mb-4">{{ $t('nav.reservations') }}</h2>
            <div v-if="loading" class="text-center py-4">
                <div class="spinner-border text-primary" role="status"></div>
            </div>
            <div v-else-if="reservations.length === 0" class="alert alert-info">
                {{ $t('reservation.no_reservations') }}
            </div>
            <div v-else>
                <div v-for="r in reservations" :key="r.id" class="card mb-3">
                    <div class="card-body">
                        <div class="d-flex justify-content-between align-items-start">
                            <div>
                                <h5>{{ r.facility_name || ('#' + r.facility_id) }}</h5>
                                <p class="mb-1"><strong>{{ $t('reservation.date') }}:</strong> {{ r.reserved_date }} {{ r.start_time }} - {{ r.end_time }}</p>
                                <p class="mb-1"><strong>{{ $t('reservation.people') }}:</strong> {{ r.number_of_people }}{{ $t('reservation.person') }}</p>
                                <span :class="['badge', statusBadge(r.status)]">{{ statusLabel(r.status) }}</span>
                                <span v-if="r.payment_status" :class="['badge', r.payment_status === 'paid' ? 'bg-success' : 'bg-warning', 'ms-1']">
                                    {{ r.payment_status === 'paid' ? $t('payment.complete') : $t('payment.unpaid') }}
                                </span>
                            </div>
                            <div>
                                <a href="#" class="btn btn-outline-primary btn-sm me-1" @click="$root.navigate('/reservation?id=' + r.id)">
                                    {{ $t('facility.detail') }}
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    `,
    data() {
        return { reservations: [], loading: true };
    },
    methods: {
        statusBadge(status) {
            return { pending: 'bg-warning', confirmed: 'bg-success', cancelled: 'bg-secondary' }[status] || 'bg-secondary';
        },
        statusLabel(status) {
            const labels = {
                pending: this.$t('reservation.status_pending'),
                confirmed: this.$t('reservation.status_confirmed'),
                cancelled: this.$t('reservation.status_cancelled')
            };
            return labels[status] || status;
        },
        async fetchReservations() {
            try {
                const result = await apiFetch('/api/reservations');
                this.reservations = result.items;
            } catch (e) {
                console.error(e);
            } finally {
                this.loading = false;
            }
        }
    },
    mounted() {
        this.fetchReservations();
    }
};
