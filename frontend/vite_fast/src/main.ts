import { createApp } from 'vue'
import { createPinia } from 'pinia'
import GAuth from 'vue3-google-oauth2'

import App from './App.vue'
import router from './router'

import './assets/index.css'

// TODO : envから"clientId"取得する
const gAuthOptions = { clientId: 'a', scope: 'email', prompt: 'consent', fetch_basic_profile: false }
const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(GAuth, gAuthOptions)


app.mount('#app')
