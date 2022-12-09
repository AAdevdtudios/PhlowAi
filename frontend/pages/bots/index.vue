<template>
    <div class="contents">
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
    </div>
</template>