<template>
    <div class="screen">
        <div class="side-bar">
            <Logo/>
            <ul>
                <li>Home</li>
                <li>Store</li>
                <li>Bots</li>
            </ul>
        </div>
        <div class="dash">
            <slot/>
        </div>
    </div>
</template>

<style>
.logo{
    @apply w-52 fill-white text-center mx-auto mb-10
}
.screen{
    @apply min-h-screen flex gap-2
}
.side-bar{
    @apply min-h-screen basis-[25%] bg-slate-900 text-white px-4 text-left py-10
}
.dash{
    @apply min-h-screen basis-[75%] bg-white py-10
}
</style>