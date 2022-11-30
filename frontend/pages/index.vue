<template>
    <div class="body_login">
        <div class="left-side">
            <Logo/>
            <RegistrationLogin v-if="show"/>
            <RegistrationRegister v-else/>
            <div class="sign-up-btn">
                <button>Don't have an account? <span>Sign Up</span></button>
            </div>
        </div>
        <div class="right-side">
            side
        </div>
    </div>
</template>

<script setup lang="ts">
var show = ref(false)
definePageMeta({
    layout: 'empty'
})
</script>