<template>
    <div>
        <div class="border-b bottom-4 flex justify-between items-center">
            <h2 class="text-2xl font-bold text-slate-900 pb-2">Purchase</h2> 
            <span class="text-slate-900 font-bold text-sm">click here for price features</span>
        </div>
        <ul class="grid gap-6 w-full md:grid-cols-2 my-3">
            <li>
                <input type="radio" id="chat-small" name="chat" value="chat-small" class="hidden peer"
                    required>
                <label for="chat-small"
                    class="inline-flex justify-between items-center p-5 w-full text-gray-500 bg-white rounded-lg border border-gray-200 cursor-pointer peer-checked:border-blue-600 peer-checked:text-blue-600 hover:text-gray-600 hover:bg-gray-100">
                    <div class="block">
                        <h1>Basic plan</h1>
                        <div class="w-full text-lg font-semibold">$10</div>
                        <div class="w-full">Best for small businesses</div>
                    </div>
                    <svg aria-hidden="true" class="ml-3 w-6 h-6" fill="currentColor" viewBox="0 0 20 20"
                        xmlns="http://www.w3.org/2000/svg">
                        <path fill-rule="evenodd"
                            d="M12.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-2.293-2.293a1 1 0 010-1.414z"
                            clip-rule="evenodd"></path>
                    </svg>
                </label>
            </li>
            <li>
                <input type="radio" id="chat-company" name="chat" value="chat-company" class="hidden peer"
                    required>
                <label for="chat-company"
                    class="inline-flex justify-between items-center p-5 w-full text-gray-500 bg-white rounded-lg border border-gray-200 cursor-pointer peer-checked:border-blue-600 peer-checked:text-blue-600 hover:text-gray-600 hover:bg-gray-100">
                    <div class="block">
                        <h1>Cooperate plan</h1>
                        <div class="w-full text-lg font-semibold">$120</div>
                        <div class="w-full">Best for Startups</div>
                    </div>
                    <svg aria-hidden="true" class="ml-3 w-6 h-6" fill="currentColor" viewBox="0 0 20 20"
                        xmlns="http://www.w3.org/2000/svg">
                        <path fill-rule="evenodd"
                            d="M12.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-2.293-2.293a1 1 0 010-1.414z"
                            clip-rule="evenodd"></path>
                    </svg>
                </label>
            </li>
            <li class="col-span-full">
                <input type="radio" id="chat-PAYC" name="chat" value="chat-PAYC" class="hidden peer">
                <label for="chat-PAYC"
                    class="inline-flex justify-between items-center p-5 w-full text-gray-500 bg-white rounded-lg border border-gray-200 cursor-pointer peer-checked:border-blue-600 peer-checked:text-blue-600 hover:text-gray-600 hover:bg-gray-100 ">
                    <div class="block">
                        <h1>Pay-as-you-go</h1>
                        <div class="w-full text-lg font-semibold">$10-upper</div>
                        <div class="w-full">Best for Growing businesses</div>
                    </div>
                    <svg aria-hidden="true" class="ml-3 w-6 h-6" fill="currentColor" viewBox="0 0 20 20"
                        xmlns="http://www.w3.org/2000/svg">
                        <path fill-rule="evenodd"
                            d="M12.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-2.293-2.293a1 1 0 010-1.414z"
                            clip-rule="evenodd"></path>
                    </svg>
                </label>
            </li>
        </ul>
    </div>
</template>

<script setup lang="ts">

</script>