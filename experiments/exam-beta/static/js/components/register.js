const RegisterPage = {
    template: `
        <div class="row justify-content-center">
            <div class="col-md-6 col-lg-4">
                <h2 class="mb-4">{{ $t('auth.register_title') }}</h2>
                <form @submit.prevent="handleRegister">
                    <div class="mb-3">
                        <label class="form-label">{{ $t('auth.username') }}</label>
                        <input v-model="form.username" class="form-control" required>
                    </div>
                    <div class="mb-3">
                        <label class="form-label">{{ $t('auth.email') }}</label>
                        <input v-model="form.email" type="email" class="form-control" required>
                    </div>
                    <div class="mb-3">
                        <label class="form-label">{{ $t('auth.password') }}</label>
                        <input v-model="form.password" type="password" class="form-control" required minlength="6">
                    </div>
                    <div class="mb-3">
                        <label class="form-label">{{ $t('auth.display_name') }}</label>
                        <input v-model="form.display_name" class="form-control">
                    </div>
                    <div v-if="error" class="alert alert-danger">{{ error }}</div>
                    <div v-if="errors" class="alert alert-danger">
                        <div v-for="(msg, key) in errors" :key="key">{{ msg }}</div>
                    </div>
                    <button type="submit" class="btn btn-primary w-100">{{ $t('auth.register_button') }}</button>
                </form>
                <p class="mt-3 text-center">
                    {{ $t('auth.has_account') }} <a href="#" @click="$root.navigate('/login')">{{ $t('auth.login_link') }}</a>
                </p>
            </div>
        </div>
    `,
    data() {
        return {
            form: { username: '', email: '', password: '', display_name: '' },
            error: null,
            errors: null
        };
    },
    methods: {
        async handleRegister() {
            try {
                const lang = i18n.global.locale;
                await apiFetch('/api/auth/register', {
                    method: 'POST',
                    body: JSON.stringify({ ...this.form, language: lang })
                });
                this.$root.navigate('/login');
            } catch (e) {
                this.errors = e.errors || null;
                this.error = e.detail || this.$t('common.error');
            }
        }
    }
};
