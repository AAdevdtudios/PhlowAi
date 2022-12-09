<template>
    <div class="table-item">
        <h2>{{ name }}</h2>
        <span>{{ active }}</span>
        <span>{{ created }}</span>
        <span>{{ edited }}</span>
        <span class="text-end more-btn">
            <button @click="more = !more">
                <img src="/icons/menu.png" alt="" />
            </button>
            <div v-show="more" class="more-items" @mouseleave="more = !more">
                <ul>
                    <li>View</li>
                    <li>Edit</li>
                    <li>Delete</li>
                </ul>
            </div>
        </span>
    </div>
</template>

<script setup lang="ts">
let more = ref(false)

interface Props {
    name: string,
    active: boolean,
    created: string,
    edited: string
}
defineProps<Props>()
</script>