const LoginPage = {
    template: `
        <div class="row justify-content-center">
            <div class="col-md-6 col-lg-4">
                <h2 class="mb-4">{{ $t('auth.login_title') }}</h2>
                <form @submit.prevent="handleLogin">
                    <div class="mb-3">
                        <label class="form-label">{{ $t('auth.username') }}</label>
                        <input v-model="username" class="form-control" required>
                    </div>
                    <div class="mb-3">
                        <label class="form-label">{{ $t('auth.password') }}</label>
                        <input v-model="password" type="password" class="form-control" required>
                    </div>
                    <div v-if="error" class="alert alert-danger">{{ error }}</div>
                    <button type="submit" class="btn btn-primary w-100">{{ $t('auth.login_button') }}</button>
                </form>
                <p class="mt-3 text-center">
                    {{ $t('auth.no_account') }} <a href="#" @click="$root.navigate('/register')">{{ $t('auth.register_link') }}</a>
                </p>
            </div>
        </div>
    `,
    data() {
        return { username: '', password: '', error: null };
    },
    methods: {
        async handleLogin() {
            try {
                const result = await apiFetch('/api/auth/login', {
                    method: 'POST',
                    body: JSON.stringify({ username: this.username, password: this.password })
                });
                store.user = result.user;
                this.$root.navigate('/');
            } catch (e) {
                this.error = e.detail || this.$t('common.error');
            }
        }
    }
};
