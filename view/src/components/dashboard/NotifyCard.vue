<template>
    <div class="flex w-full gap-4 items-center bg-white p-2 border-y border-slate-300">
        <font-awesome-icon 
            icon="fa-solid fa-reply"
            class="p-2 bg-yellow-100 text-amber-500 rounded-full text-sm md:text-base lg:text-lg" 
            v-if="type === 'reply'" 
        />

        <font-awesome-icon 
            icon="fa-solid fa-thumbs-up"
            class="p-2 bg-blue-100 text-blue-500 rounded-full text-sm md:text-base lg:text-lg" 
            v-else-if="type === 'approve'" 
        />

        <font-awesome-icon 
            icon="fa-solid fa-comment"
            class="p-2 bg-green-100 text-green-600 rounded-full text-sm md:text-base lg:text-lg" 
            v-else-if="type === 'receive'" 
        />

        <font-awesome-icon 
            icon="fa-solid fa-ban"
            class="p-2 bg-red-100 text-red-500 rounded-full text-sm md:text-base lg:text-lg" 
            v-else-if="type === 'deny'" 
        />

        <font-awesome-icon 
            icon="fa-solid fa-bell"
            class="p-2 bg-purple-100 text-purple-400 rounded-full text-sm md:text-base lg:text-lg" 
            v-else-if="type === 'suggest'" 
        />

        <div>
            <span class="flex items-center justify-center gap-2 ">
                <h2 class="text-xs md:text-sm lg:text-base font-semibold text-sky-900">{{ title }}</h2>
                <p class="text-xs lg:text-sm text-slate-500 hover:text-green-600 hover:cursor-pointer">{{ subtitle }}</p>
            </span>
            <p class="text-xs lg:text-sm text-slate-500">{{ time }}</p>
        </div>
    </div>
</template>

<script lang="ts">
export default {
    props: {
        title: {
            type: String,
            required: true
        },
        subtitle: {
            type: String,
            required: true
        },
        time: {
            type: String,
            required: true
        },
        type: {
            type: String,
            required: true
        }
    }
}
</script>