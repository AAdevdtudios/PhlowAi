<template>
    <div class="overflow-x-hidden">
        <slot/>
    </div>
</template>

<style>
.logo{
    @apply w-40 mb-5
}
.left-side{
    @apply bg-white/10 md:basis-2/4 m-auto px-6 md:px-[70px]
}
.right-side{
    @apply bg-slate-900 basis-2/4 hidden md:block
}
.body_login{
    @apply flex w-screen h-screen
}
.buttons{
    @apply grid grid-cols-2 gap-2
}
.disable{
    @apply bg-slate-900 text-white
}
.active{
    @apply bg-slate-900/20 text-white
}
.holder {
    @apply text-left w-full space-y-2
}
.sign-up-btn{
    @apply text-center mt-4
}
.sign-up-btn span{
    @apply text-slate-900 font-bold
}
.btn-list{
    @apply grid md:grid-cols-2 items-center
}
.btn-list button{
    @apply bg-slate-900 text-white mt-5 md:mt-0 py-2 md:ml-40 rounded-md hover:bg-slate-800
}
.radio-btn{
    @apply flex gap-3
}
.forgot-password{
    @apply text-right text-slate-900 font-bold border-b-2 border-r-slate-900 pb-3
}
.holder h4 {
    @apply font-bold text-slate-900 text-2xl mb-1
}

.holder .welcome {
    @apply text-gray-500
}

.input-holder {
    @apply flex flex-col items-start md:grid grid-cols-3 md:items-center
}

.input-holder input {
    @apply bg-slate-100 w-full p-2 col-span-2 rounded-lg focus:border-2 focus:border-slate-700 mt-3 md:mt-0
}

.input-box {
    @apply mt-10 space-y-5
}
</style>