<template>
    <div class="contents account-contents">
        <div class="account-box">
            <div class="header-edit">
                <span>Account information</span>
                <div>
                    <button v-if="accountInfo" @click="accountInfo=!accountInfo">
                        Edit
                    </button>
                    <button v-else @click="saveInfo()">
                        Save
                    </button>
                </div>
            </div>
            <label for="Name" class="account-info">
                <span>Name</span>
                <input type="name" placeholder="Users name" :disabled="accountInfo">
            </label>
            <label for="Name" class="account-info">
                <span>Email</span>
                <input type="name" placeholder="Users email" :disabled="accountInfo">
            </label>
            <label for="Name" class="account-info">
                <span>Phone number</span>
                <input type="name" placeholder="+2349015113123" :disabled="accountInfo">
            </label>
            <label for="Name" class="account-info">
                <span>Company name</span>
                <input type="name" placeholder="Users email" :disabled="accountInfo">
            </label>
            <label for="Name" class="account-info">
                <span>Phone number</span>
                <input type="name" placeholder="+2349015113123" :disabled="accountInfo">
            </label>
        </div>
        <div class="integration-box">
            <div class="header-edit">
                <span>Integrate PhlowAi with your social media </span>
                <div>
                    <button v-if="integrationEdit" @click="(integrationEdit=!integrationEdit)">
                        Edit
                    </button>
                    <button v-else @click="saveIntegration()">
                        Save
                    </button>
                </div>
            </div>
            <label for="Name" class="account-info">
                <span>Api Key</span>
                <div class="inputs">
                    <button class="generate">
                        Generate
                    </button>
                    <input type="text" disabled placeholder="This is a long key but it is for testing" class="apiKey">
                    <button class="copy" @click="copy()">
                        Copy
                    </button>
                </div>
            </label>
            <label for="Name" class="account-info">
                <span>Telegram Key</span>
                <input type="name" placeholder="Telegram api Key" :disabled="integrationEdit">
            </label>
            <label for="Name" class="account-info">
                <span>Twilo Key for Whatsapp</span>
                <input type="name" placeholder="Twilo Api key" :disabled="integrationEdit">
            </label>
            <label for="Name" class="account-info">
                <span>Facebook key</span>
                <input type="name" placeholder="Facebook Api Key" :disabled="integrationEdit">
            </label>
            <label for="Name" class="account-info">
                <span>Discord key</span>
                <input type="name" placeholder="Discord Api Key" :disabled="integrationEdit">
            </label>
        </div>
        <div v-show="false" class="message-box">
            <p>Welcome</p>
        </div>
    </div>
</template>

<script lang="ts" setup>
var accountInfo = ref(true)
var integrationEdit = ref(true)

function saveInfo(){
    console.log("Do this first");
    accountInfo.value = true;
}
function copy(){
    //this.$snack.metodo('My Message') 
    navigator.clipboard.writeText("Hello boys")
}
function saveIntegration(){
    integrationEdit.value = true;
}

</script>