<template>
    <li class="flex items-center">
        <div class="flex items-center gap-2">
            <span>
                <h2 class="text-xs md:text-sm lg:text-base font-semibold text-sky-900" v-if="!isEditting">
                    {{ name }}
                </h2>
                <input type="text" class="text-xs md:text-sm lg:text-base px-2 py-1 mb-1 border border-sky-950 text-black w-full" v-else :value="name" @input="$emit('update:name', ($event.target as HTMLInputElement).value)" />

                <p class="text-gray-500 text-xs lg:text-sm" v-if="!isEditting">
                    {{ level }}
                </p>
                <input type="text" class="text-xs md:text-sm lg:text-base px-2 py-1 mb-1 border border-sky-950 text-black w-full" v-else :value="level" @input="$emit('update:level', ($event.target as HTMLInputElement).value)" />

            </span>
            <font-awesome-icon icon="fa-solid fa-xmark" v-if="isEditting" class="text-green-700 hover:cursor-pointer" @click="deleteLanguage(id)"/>
        </div>
    </li>
</template>

<script lang="ts">
    export default {
        emits: [
            "update:name",
            "update:level",
            "delete-language"
        ],
        props: {
            id: {
                type: Number,
                required: true,
            },
            isEditting: {
                type: Boolean,
                default: false,
            },
            name: {
                type: String,
                required: true,
            },
            level: {
                type: String,
                required: true,
            },
        },
        methods: {
            deleteLanguage(id: Number) {
                this.$emit("delete-language", id);
            },
        }
    }
</script>