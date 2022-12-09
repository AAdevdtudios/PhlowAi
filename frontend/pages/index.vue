<template>
    <div class="body_login">
        <div class="left-side">
            <Logo/>
            <RegistrationLogin v-if="showLogin"/>
            <RegistrationRegister v-else/>
            <div class="sign-up-btn">
                <button @click="showLogin = !showLogin">
                    <div v-if="showLogin">Don't have an account? <span>Sign Up</span></div>
                    <div v-else>Already have an account? <span>Sign In</span></div>
                </button>
            </div>
        </div>
        <div class="right-side">
            side
        </div>
    </div>
</template>

<script setup lang="ts">
let showLogin = ref<boolean>(true);

definePageMeta({
    layout: 'empty'
})
</script>