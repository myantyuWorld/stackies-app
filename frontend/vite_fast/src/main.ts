import { createApp } from 'vue'
import App from './App.vue'
import { createPinia } from 'pinia'
import gAuthPlugin from 'vue3-google-oauth2'
import router from './router'

import './assets/index.css'

// TODO : envから"clientId"取得する
const gAuthOptions = { clientId: '12529638050-iedqhf79ojumba2evm3g6p85pa6st1js.apps.googleusercontent.com', scope: 'email', prompt: 'consent', fetch_basic_profile: true }
const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(gAuthPlugin, gAuthOptions)


app.mount('#app')
