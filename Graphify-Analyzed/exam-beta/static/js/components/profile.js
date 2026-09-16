const ProfilePage = {
    template: `
        <div class="row justify-content-center">
            <div class="col-md-6">
                <h2 class="mb-4">{{ $t('profile.title') }}</h2>
                <form @submit.prevent="handleUpdate">
                    <div class="mb-3">
                        <label class="form-label">{{ $t('auth.display_name') }}</label>
                        <input v-model="form.display_name" class="form-control" required>
                    </div>
                    <div class="mb-3">
                        <label class="form-label">{{ $t('auth.email') }}</label>
                        <input v-model="form.email" type="email" class="form-control" required>
                    </div>
                    <div class="mb-3">
                        <label class="form-label">{{ $t('profile.language') }}</label>
                        <select v-model="form.language" class="form-select">
                            <option value="ja">日本語</option>
                            <option value="en">English</option>
                            <option value="zh">中文</option>
                        </select>
                    </div>
                    <div v-if="message" class="alert alert-success">{{ message }}</div>
                    <div v-if="error" class="alert alert-danger">{{ error }}</div>
                    <button type="submit" class="btn btn-primary">{{ $t('common.save') }}</button>
                </form>
            </div>
        </div>
    `,
    data() {
        return {
            form: { ...store.user },
            message: null,
            error: null
        };
    },
    methods: {
        async handleUpdate() {
            try {
                const result = await apiFetch('/api/auth/profile', {
                    method: 'PUT',
                    body: JSON.stringify(this.form)
                });
                store.user = result.user;
                if (this.form.language !== i18n.global.locale) {
                    this.$root.setLanguage(this.form.language);
                }
                this.message = this.$t('profile.updated');
            } catch (e) {
                this.error = e.detail || this.$t('common.error');
            }
        }
    }
};
