<template>
    <div class="holder">
        <div>
            <h4>Create Account</h4>
            <span class="welcome">Get access to exclusive features by creating an account</span>
        </div>
        <component :is="tab"></component>
        <div class="buttons">
            <button class="p-2 rounded-md" :class="tabNo<=1? 'active':'disable'" @click="prev" :disabled="tabNo<=1">Previous</button>
            <button class="p-2 rounded-md" :class="tabNo >= 3? 'active':'disable'" @click="next" :disabled="tabNo >= 3">Next</button>
        </div>
    </div>
</template>
<script setup lang="ts">
var tab = shallowRef(resolveComponent("TabsPricing"))
const tabNo = ref(1);

function change (){
    var currentTab;
    switch (tabNo.value) {
        case 1:
            currentTab = resolveComponent("TabsPricing")
            break;
        case 2:
            currentTab = resolveComponent("TabsRegisterForm")
            break;
        case 3:
            currentTab = resolveComponent("TabsPayment")
            break;
    
        default:
            currentTab = resolveComponent("TabsPricing")
            break;
    }
    tab.value = currentTab;
}
function next(){
    tabNo.value ++;
    change()
}
function prev() {
    tabNo.value --;
    change()
}
</script>