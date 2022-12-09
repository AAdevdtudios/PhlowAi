<template>
    <div class="screen">
        <div class="side-bar">
            <Logo />
            <div class="nav-links">
                <nuxt-link to="/dashboard">
                    <img src="/icons/home.png" alt="">
                        <span>Dashboard</span>
                </nuxt-link>
                <nuxt-link to="/bots">
                    <img src="/icons/mind-map.png" alt="">
                    <span>Bots</span>
                </nuxt-link>
                <nuxt-link to="/stores">
                    <img src="/icons/store.png" alt="">
                    <span>Stores</span>
                </nuxt-link>
                <nuxt-link to="/account">
                    <img src="/icons/account.png" alt="">
                    <span>Accounts</span>
                </nuxt-link>
            </div>
        </div>
        <div class="dash">
            <div class="header">
                <h2>{{routes.name}}</h2>
                <div class="nav-actions">
                    <nuxt-link to="/account">
                        <img src="/icons/user.png" class="account" />
                    </nuxt-link>
                </div>
            </div>
            <slot />
        </div>
    </div>
</template>

<script setup lang="ts">
const routes = useRoute()
const themeMode = ref(true)

</script>

<style>
::-webkit-scrollbar{
    display: none;
}
.logo{
    @apply w-52 fill-white text-center mx-auto mb-10 px-10
}
.screen{
    @apply min-h-screen flex
}
.side-bar{
    @apply max-h-screen basis-[10%] bg-slate-900 text-white text-left py-10 sticky left-0 top-0
}
.side-bar .nav-links{
    @apply flex flex-col space-y-4 font-bold font-workSans
}
.nav-links img{
    @apply w-10 h-10 p-2 rounded-md anim
}
.nav-links .router-link-active img{
    @apply bg-yellow-400
}
.nav-links a{
    @apply w-full p-3 flex items-center gap-3 text-white opacity-20 hover:opacity-100 anim
}
.nav-links .router-link-active{
    @apply opacity-100
}
.router-link-active{
    @apply text-blue-500 bg-slate-800
}
.dash{
    @apply min-h-screen basis-[90%] bg-white anim
}
h2{
    @apply font-semibold text-[1.3rem] font-workSans
}
.header h2{
    @apply capitalize
}
.account{
    @apply bg-slate-800/90 rounded-full h-7 w-7 p-1
}
.contents{
    @apply flex flex-col px-10 overflow-y-scroll min-h-screen pt-3 pb-20
}
.header{
    @apply flex justify-between bg-white items-center px-10 shadow-md py-4 sticky top-0 left-0 z-50
}
.header .nav-actions{
    @apply flex gap-4
}
.toggle-label{
    @apply inline-flex relative items-center cursor-pointer font-workSans
}
.toggle-label div{
    @apply w-11 h-6 bg-gray-900 rounded-full after:content-[''] after:absolute after:top-[3px] after:left-[2px] after:bg-white after:border-gray-300 after:rounded-full after:h-5 after:w-5 after:transition-all after:ease-in-out
}
.toggle-label span{
    @apply ml-3 text-sm font-medium text-gray-900
}
.btn-controls{
    @apply flex justify-between items-center py-5
}
.btn-dash{
    @apply space-x-2
}
.bot{
    @apply font-semibold font-workSans px-10 py-2 rounded hover:bg-slate-900/20 anim
}
.btn-dash .active{
    @apply bg-slate-900 text-pri
}
.store-btn{
    @apply font-semibold font-workSans px-10 py-2 rounded border border-slate-900 hover:bg-yellow-100
}
.anim{
    @apply transition-all ease-linear delay-200
}
.table-header{
    @apply grid grid-cols-6 space-x-5 font-workSans text-sm text-slate-800 items-center my-3 mx-6
}
.table-header button{
    @apply h-9 w-9 p-2 bg-slate-900 cursor-pointer hover:bg-slate-700 rounded-md anim
}
.name-head{
    @apply col-span-2
}
.info-box{
    @apply w-full pt-4 px-10 py-5 bg-slate-900 border border-sky-300 rounded-lg text-white font-workSans relative flex space-x-10
}
.info-box .text-items{
    @apply max-w-2xl flex items-start flex-col justify-center
}
.info-box .text-items h1{
    @apply font-bold text-4xl mb-5
}
.info-box .text-items .username{
    @apply text-pri
}
.info-box img{
    @apply w-[20%] h-[159px]
}
.info-box .items{
    @apply flex flex-col 
}
.items h4{
    @apply font-bold font-workSans text-slate-900
}
.spin-ring{
    @apply ring ring-slate-900 rounded-md
}
.item-flex{
    @apply flex flex-1 gap-2
}
.item-flex .right{
    @apply flex items-center
}
.item-flex .activities{
    @apply flex gap-1 items-center font-workSans
}
.item-flex .activities .box{
    @apply h-4 w-4 rounded
}
.table-item{
    @apply grid grid-cols-6 space-x-5 font-workSans text-sm text-slate-800 items-center px-6 bg-slate-600/10 py-4 my-2 font-bold
}
.table-item h2{
    @apply col-span-2
}
.table-item button{
    @apply h-9 w-9 p-2 bg-slate-800/10 cursor-pointer hover:bg-slate-700/30 rounded-md anim relative
}
.table-item .exs{
    @apply grid grid-cols-4 items-center space-x-[3.7rem] basis-[80%]
}
.more-items{
    @apply bg-white z-20 p-3 absolute shadow-md shadow-slate-900/10 text-left space-x-2 anim  left-10 -top-20
}
.more-btn{
    @apply relative
}
.more-items ul li {
    @apply hover:bg-slate-900 anim hover:text-white p-2 rounded cursor-pointer
}
.filter{
    @apply space-x-5 font-workSans
}
.filter select{
    @apply p-2 font-bold rounded-md bg-slate-900 text-white
}
.account-contents{
    @apply space-y-8
}
.account-box{
    @apply min-h-full p-3 grid grid-cols-3 gap-2 gap-y-5 font-workSans font-medium shadow-md shadow-gray-100 rounded-md py-10
}
.account-info{
    @apply flex flex-col justify-start
}
.header-edit{
    @apply col-span-full flex items-baseline space-x-20 font-bold text-2xl border-b pb-5 justify-between font-workSans
}
.header-edit button{
    @apply text-base bg-slate-900 px-5 text-white font-medium rounded py-2
}
.account-info input{
    @apply p-4 disabled:bg-slate-800/20 rounded-lg bg-slate-200 outline-none font-bold
}
.account-info .apiKey{
    @apply disabled:bg-transparent pl-0 flex-1
}
.account-info .inputs{
    @apply w-full flex bg-gray-300 overflow-hidden rounded-md
}
.inputs .generate{
    @apply bg-slate-900 text-white px-2
}
.inputs .copy{
    @apply bg-slate-900 text-white px-2
}
.account-info button{
    @apply h-full hover:bg-slate-900/70 anim
}
.message-box{
    @apply top-1/2 left-1/2 -translate-y-1/2 -translate-x-1/2 p-3 rounded-md w-fit bg-slate-900/90 text-white fixed anim
}
.account-info span{
    @apply mb-3
}
.integration-box{
    @apply grid grid-cols-3 gap-4 py-5 font-workSans font-medium
}
</style>