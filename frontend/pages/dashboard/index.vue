<template>
    <div class="contents">
        <div class="info-box">
            <img src="/images/chatting.svg" alt="">
            <div class="text-items">
                <h1>Welcome <span class="username">Username</span></h1>
                <span>Create your chatbot using our effective drag and drop system and unique templates that fit your
                    business needs </span>
            </div>
        </div>
        <div class="btn-controls">
            <div class="btn-dash">
                <button @click="setActive = true" class="bot" :class="setActive ? 'active':''">Bots</button>
                <button @click="setActive = false" class="bot" :class="setActive ? '' : 'active'">Stores</button>
            </div>
            <div class="filter">
                <span>Sort by:</span>
                <select>
                    <option value="edited">date edited</option>
                    <option value="created anim">date Created</option>
                </select>
            </div>

        </div>
        <div class="table-header">
            <span class="name-head">Name</span>
            <span>Active</span>
            <span>Created on</span>
            <span>Edited on</span>
            <span class="text-end">
                <button>
                    <img src="/icons/plus.png" alt="" />
                </button>
            </span>
        </div>
        <TableItems created="28 July 2022" edited="28 November 2022" name="Trial bot" :active="false" />
        <TableItems created="28 July 2022" edited="28 November 2022" name="Trial bot" :active="false" />
        <TableItems created="28 July 2022" edited="28 November 2022" name="Trial bot" :active="false" />
        <TableItems created="28 July 2022" edited="28 November 2022" name="Trial bot" :active="false" />
        <TableItems created="28 July 2022" edited="28 November 2022" name="Trial bot" :active="false" />
        <TableItems created="28 July 2022" edited="28 November 2022" name="Trial bot" :active="false" />
        <TableItems created="28 July 2022" edited="28 November 2022" name="Trial bot" :active="false" />
        <TableItems created="28 July 2022" edited="28 November 2022" name="Trial bot" :active="false" />
        <TableItems created="28 July 2022" edited="28 November 2022" name="Trial bot" :active="false" />
        <TableItems created="28 July 2022" edited="28 November 2022" name="Trial bot" :active="false" />
        <TableItems created="28 July 2022" edited="28 November 2022" name="Trial bot" :active="false" />
        <TableItems created="28 July 2022" edited="28 November 2022" name="Trial bot" :active="false" />
        <TableItems created="28 July 2022" edited="28 November 2022" name="Trial bot" :active="false" />
        <TableItems created="28 July 2022" edited="28 November 2022" name="Trial bot" :active="false" />
    </div>
</template>

<script setup lang="ts">
let setActive = ref(true)
</script>