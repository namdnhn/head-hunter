<template>
	<div class="p-8 md:basis-3/5 lg:basis-4/5 flex flex-col gap-10" id="chat-page">
		<h1 class="text-lg md:text-xl lg:text-2xl text-sky-900 font-bold">
			Tin nhắn
		</h1>
		<div class="bg-white w-full p-4 flex gap-4">
			<!-- list message  -->
			<div class="flex flex-col gap-4 basis-1/5">
				<message-card></message-card>
				<message-card></message-card>
				<message-card></message-card>
			</div>

			<div class="basis-4/5 bg-green-50 flex flex-col gap-4 p-4 relative" id="chat-box">
                <div class="flex flex-col gap-2">
                    <receive-message></receive-message>
                    <receive-message></receive-message>
                    <receive-message></receive-message>
                    <sent-message></sent-message>
                    <sent-message></sent-message>
                    <sent-message></sent-message>
                    <sent-message></sent-message>
                    <sent-message></sent-message>
                    <sent-message></sent-message>
                    <sent-message></sent-message>
                    <sent-message></sent-message>
                    <sent-message></sent-message>
                    <sent-message></sent-message>
                    <sent-message></sent-message>
                    <sent-message></sent-message>
                    <sent-message></sent-message>
                    <sent-message></sent-message>
                    <sent-message></sent-message>
                </div>

                <div class="flex gap-4 text-xs md:text-sm lg:text-base">
                    <input type="text" class="w-full border border-gray-300 rounded-lg p-2.5" placeholder="Nhập tin nhắn của bạn ..."/>
                    <button class=" bg-green-400 p-4 rounded-xl font-bold text-sky-900 hover:bg-green-500">Gửi</button>
                </div>
			</div>
		</div>
	</div>
</template>

<script lang="ts">
import MessageCard from "../../components/dashboard/message/MessageCard.vue";
import ReceiveMessage from "../../components/dashboard/message/ReceiveMessage.vue";
import SentMessage from "../../components/dashboard/message/SentMessage.vue";
export default {
	components: {
		MessageCard,
        ReceiveMessage,
        SentMessage
	}
};
</script>

<style scoped>
#chat-page {
    max-height: 760px;
}
#chat-box {
    overflow-y: scroll;
    max-height: 600px;
    min-height: 600px;
}
</style>