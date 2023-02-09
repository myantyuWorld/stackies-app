<template>
    <section class="bg-gray-100 dark:bg-gray-900">
        <div class="flex flex-col items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0">
            <a href="#" class="flex items-center mb-6 text-2xl font-semibold text-gray-900 dark:text-white"
                :class="[isShowLoading ? 'opacity-40' : '']">

                <img alt="Vue logo" class="logo" src="@/assets/sample.jpeg" width="125" height="125" />
                Stackies!
            </a>
            <div
                class="w-full bg-white rounded-lg shadow dark:border md:mt-0 sm:max-w-md xl:p-0 dark:bg-gray-800 dark:border-gray-700">
                <Loading :is-show="isShowLoading" />
                <div class="p-6 space-y-4 md:space-y-6 sm:p-8">
                    <h1 class="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white"
                        :class="[isShowLoading ? 'opacity-40' : '']">
                        Sign in to your account
                    </h1>

                    <div class="space-y-4 md:space-y-6" :class="[isShowLoading ? 'opacity-40' : '']">
                        <div>
                            <label for="password"
                                class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Stackies!は、案件対応履歴管理アプリです。</label>
                            <label for="password"
                                class="block mb-2 text-sm font-light text-gray-900 dark:text-white">ああああああああああああああああああああああああああああああああああああああ</label>
                            <label for="password"
                                class="block mb-2 text-sm font-light text-gray-900 dark:text-white">ああああああああああああああああああああああああああああああああああああああ</label>
                        </div>

                        <button type="submit"
                            class="w-full text-white bg-blue-600 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800"
                            :class="[isShowLoading ? 'opacity-40' : '']" @click="login">
                            Signin
                        </button>
                        <button
                            class="w-full text-white bg-blue-600 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800"
                            @click="handleClickGetAuth" :disabled="!isInit">get auth code</button>
                        <button
                            class="w-full text-white bg-blue-600 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800"
                            @click="handleClickSignIn" v-if="!isSignIn" :disabled="!isInit">signIn</button>
                        <button
                            class="w-full text-white bg-blue-600 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800"
                            @click="handleClickSignOut" v-if="isSignIn" :disabled="!isInit">signOout</button>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import axios from 'axios';
import router from '@/router';

import Loading from '../components/Loading.vue'

const isInit = ref(false)
const isSignIn = ref(false)
const isShowLoading = ref(false)
console.log(import.meta.env.VITE_GOOGLE_CLIENT_ID)

const GOOGLE_CLIENT_ID = import.meta.env.VITE_GOOGLE_CLIENT_ID
const DRF_CLIENT_ID = import.meta.env.VITE_DRF_CLIENT_ID
const DRF_CLIENT_SECRET = import.meta.env.VITE_DRF_CLIENT_SECRET

const handleClickGetAuth = async () => {
    console.log('handleClickGetAuth')
    try {
        const authCode = await this.$gAuth.getAuthCode()
        const response = await this.$http.post('http://localhost:18000/auth/convert-token', { code: authCode, redirect_uri: 'postmessage' })
    } catch (error) {
        // On fail do something
    }
}

const handleClickSignIn = async () => {
    console.log('handleClickSignIn')
    try {
        const googleUser = await this.$gAuth.signIn()
        console.log('user', googleUser)
        this.isSignIn = this.$gAuth.isAuthorized
    } catch (error) {
        // On fail do something
        console.error(error);
        return null;
    }
}

const handleClickSignOut = async () => {
    console.log('handleClickSignOut')
    try {
        await this.$gAuth.signOut()
        this.isSignIn = this.$gAuth.isAuthorized
    } catch (error) {
        // On fail do something
    }
}

const login = () => {
    new Promise((resolve) => {
        isShowLoading.value = true
        setTimeout(() => {
            resolve();
        }, 3000);
    }).then(() => {
        // TODO : 共通化 | https://programmer-note.hatenablog.com/entry/2021/09/26/175427
        const promise = axios.get("http://localhost:18000/api/members/")
        promise
            .then((response) => {
                console.log(response)
                isShowLoading.value = false
                // router/index.ts > router.nameで画面遷移可能 | https://v3.router.vuejs.org/ja/guide/essentials/navigation.html
                // router.push('menu')
            })
            .catch((e) => {
                console.log(e)
            })
    });
}
</script>