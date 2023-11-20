<template>
	<main
		class="fixed top-0 left-0 right-0 w-full h-full bg-white pt-16 lg:pt-20 flex"
	>
		<!-- list chat user  -->
		<div
			class="basis-1/4 border border-e-2 overflow-y-scroll overflow-x-hidden p-2 flex flex-col gap-2"
		>
			<user-chatted></user-chatted>
			<user-chatted></user-chatted>
			<user-chatted></user-chatted>
		</div>

		<!-- chat box  -->
		<div class="basis-3/4 relative">
			<!-- header chat box  -->
			<div
				class="absolute w-full left-0 right-0 top-0 py-2 px-4 flex gap-4 items-center border border-e-2 shadow h-16"
			>
				<img
					src="https://scontent.fhan2-4.fna.fbcdn.net/v/t1.6435-1/36412437_273721143203802_2074360962202206208_n.jpg?stp=dst-jpg_p100x100&_nc_cat=105&ccb=1-7&_nc_sid=2b6aad&_nc_eui2=AeHOS_Lm8ewvSUA9lIVcAhHLrMgDE4oycXWsyAMTijJxdawX51mnh42l1bBCp7I2xJAwVfGZuGyJ629p0KsVhof5&_nc_ohc=KiZOVlAFR3YAX-k_Tvz&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.fhan2-4.fna&oh=00_AfAeuq_ZDgOVRFV_ojGB87tZarSGNykVRZX52iJbG2AddQ&oe=65819BFF"
					alt="avt"
					class="h-12 w-12 rounded-full"
				/>
				<h2
					class="lg:text-lg md:text-base text-sm font-bold text-sky-900"
				>
					Nguyễn Đức Thiện
				</h2>
			</div>

			<div
				ref="chatContainer"
				class="absolute top-16 bottom-16 w-full py-2 px-4 overflow-y-scroll flex flex-col gap-2"
			>
				<message-card
					v-for="message in messages"
					:key="message.id"
					:avt="message.avt"
					:type="message.type"
					:content="message.content"
					:time="message.time"
				></message-card>
			</div>

			<!-- input message  -->
			<div
				class="absolute w-full left-0 right-0 bottom-0 py-2 px-4 flex items-center gap-4 border border-t-2 shadow h-16"
			>
				<input
					type="text"
					class="p-2 bg-slate-200 w-full rounded-3xl lg:text-base md:text-sm text-xs"
					placeholder="Aa"
					v-model="message"
				/>
				<button
					class="p-2 bg-green-300 rounded-lg text-green-800 hover:cursor-pointer hover:bg-green-400 hover:text-green-900"
					v-if="message"
				>
					Gửi
				</button>
				<font-awesome-icon
					icon="fa-solid fa-thumbs-up"
					class="text-green-600 lg:text-xl md:text-lg text-base hover:text-green-700 hover:cursor-pointer"
					v-else
				/>
			</div>
		</div>
	</main>
</template>

<script lang="ts">
import UserChatted from "../../components/message/UserChatted.vue";
import MessageCard from "../../components/message/MessageCard.vue";
export default {
	components: {
		UserChatted,
		MessageCard,
	},
	data() {
		return {
			message: "",
			messages: [
				{
					id: 1,
					type: "received",
					avt: "https://scontent.fhan2-4.fna.fbcdn.net/v/t1.6435-1/36412437_273721143203802_2074360962202206208_n.jpg?stp=dst-jpg_p100x100&_nc_cat=105&ccb=1-7&_nc_sid=2b6aad&_nc_eui2=AeHOS_Lm8ewvSUA9lIVcAhHLrMgDE4oycXWsyAMTijJxdawX51mnh42l1bBCp7I2xJAwVfGZuGyJ629p0KsVhof5&_nc_ohc=KiZOVlAFR3YAX-k_Tvz&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.fhan2-4.fna&oh=00_AfAeuq_ZDgOVRFV_ojGB87tZarSGNykVRZX52iJbG2AddQ&oe=65819BFF",
					content: "alo alo",
					time: "12:15",
				},
				{
					id: 2,
					type: "sent",
					avt: "https://example.com/avatar2.jpg",
					content: "Hello, how are you?",
					time: "12:16",
				},
				{
					id: 3,
					type: "received",
					avt: "https://scontent.fhan2-4.fna.fbcdn.net/v/t1.6435-1/36412437_273721143203802_2074360962202206208_n.jpg?stp=dst-jpg_p100x100&_nc_cat=105&ccb=1-7&_nc_sid=2b6aad&_nc_eui2=AeHOS_Lm8ewvSUA9lIVcAhHLrMgDE4oycXWsyAMTijJxdawX51mnh42l1bBCp7I2xJAwVfGZuGyJ629p0KsVhof5&_nc_ohc=KiZOVlAFR3YAX-k_Tvz&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.fhan2-4.fna&oh=00_AfAeuq_ZDgOVRFV_ojGB87tZarSGNykVRZX52iJbG2AddQ&oe=65819BFF",
					content: "alo alo",
					time: "12:15",
				},
				{
					id: 4,
					type: "sent",
					avt: "https://example.com/avatar2.jpg",
					content: "Hello, how are you?",
					time: "12:16",
				},
				{
					id: 5,
					type: "received",
					avt: "https://scontent.fhan2-4.fna.fbcdn.net/v/t1.6435-1/36412437_273721143203802_2074360962202206208_n.jpg?stp=dst-jpg_p100x100&_nc_cat=105&ccb=1-7&_nc_sid=2b6aad&_nc_eui2=AeHOS_Lm8ewvSUA9lIVcAhHLrMgDE4oycXWsyAMTijJxdawX51mnh42l1bBCp7I2xJAwVfGZuGyJ629p0KsVhof5&_nc_ohc=KiZOVlAFR3YAX-k_Tvz&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.fhan2-4.fna&oh=00_AfAeuq_ZDgOVRFV_ojGB87tZarSGNykVRZX52iJbG2AddQ&oe=65819BFF",
					content: "alo alo",
					time: "12:15",
				},
				{
					id: 6,
					type: "sent",
					avt: "https://example.com/avatar2.jpg",
					content: "Hello, how are you?",
					time: "12:16",
				},
				{
					type: "received",
					avt: "https://scontent.fhan2-4.fna.fbcdn.net/v/t1.6435-1/36412437_273721143203802_2074360962202206208_n.jpg?stp=dst-jpg_p100x100&_nc_cat=105&ccb=1-7&_nc_sid=2b6aad&_nc_eui2=AeHOS_Lm8ewvSUA9lIVcAhHLrMgDE4oycXWsyAMTijJxdawX51mnh42l1bBCp7I2xJAwVfGZuGyJ629p0KsVhof5&_nc_ohc=KiZOVlAFR3YAX-k_Tvz&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.fhan2-4.fna&oh=00_AfAeuq_ZDgOVRFV_ojGB87tZarSGNykVRZX52iJbG2AddQ&oe=65819BFF",
					content: "alo alo",
					time: "12:15",
				},
				{
					id: 7,
					type: "sent",
					avt: "https://example.com/avatar2.jpg",
					content: "Hello, how are you?",
					time: "12:16",
				},
				{
					id: 8,
					type: "received",
					avt: "https://scontent.fhan2-4.fna.fbcdn.net/v/t1.6435-1/36412437_273721143203802_2074360962202206208_n.jpg?stp=dst-jpg_p100x100&_nc_cat=105&ccb=1-7&_nc_sid=2b6aad&_nc_eui2=AeHOS_Lm8ewvSUA9lIVcAhHLrMgDE4oycXWsyAMTijJxdawX51mnh42l1bBCp7I2xJAwVfGZuGyJ629p0KsVhof5&_nc_ohc=KiZOVlAFR3YAX-k_Tvz&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.fhan2-4.fna&oh=00_AfAeuq_ZDgOVRFV_ojGB87tZarSGNykVRZX52iJbG2AddQ&oe=65819BFF",
					content: "alo alo",
					time: "12:15",
				},
				{
					id: 9,
					type: "sent",
					avt: "https://example.com/avatar2.jpg",
					content: "Hello, how are you?",
					time: "12:16",
				},
                {
					id: 10,
					type: "sent",
					avt: "https://example.com/avatar2.jpg",
					content: "Hello, how are you?",
					time: "12:16",
				},
                {
					id: 11,
					type: "sent",
					avt: "https://example.com/avatar2.jpg",
					content: "Hello, how are you?",
					time: "12:16",
				},
                {
					id: 12,
					type: "sent",
					avt: "https://example.com/avatar2.jpg",
					content: "Hello, how are you?",
					time: "12:16",
				},
                {
					id: 13,
					type: "sent",
					avt: "https://example.com/avatar2.jpg",
					content: "Hello, how are you?",
					time: "12:16",
				},
			],
		};
	},
	mounted() {
		this.$nextTick(function () {
			const chatContainer = this.$refs.chatContainer as HTMLDivElement;
			chatContainer.scrollTop = chatContainer.scrollHeight;
		});
	},
};
</script>
