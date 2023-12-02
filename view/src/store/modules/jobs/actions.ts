export default {
	async getJobs() {
		let apiUrl = "http://localhost:3000/jobs";

		const response = await fetch(apiUrl, {
			method: "GET",
			headers: {
				"Content-Type": "application/json",
			},
		});

		const responseData = await response.json();

		if (!response.ok) {
			const error = new Error(
				responseData.message || "Failed to fetch jobs."
			);
			throw error;
		}

		return responseData;
	},
	async getJob(_: any, id: any) {
		let apiUrl = "http://localhost:3000/jobs/" + id;

		const response = await fetch(apiUrl, {
			method: "GET",
			headers: {
				"Content-Type": "application/json",
			},
		});

		const responseData = await response.json();

		if (!response.ok) {
			const error = new Error(
				responseData.message || "Failed to fetch job."
			);
			throw error;
		}

		responseData.deadline = new Date(
			responseData.deadline
		).toLocaleDateString("en-CA"); // 'en-CA' format is yyyy-mm-dd

		return responseData;
	},
	async getFeaturedJobs() {
		let apiUrl = "http://localhost:3000/featured_jobs";
		const response = await fetch(apiUrl, {
			method: "GET",
			headers: {
				"Content-Type": "application/json",
			},
		});

		const responseData = await response.json();

		if (!response.ok) {
			const error = new Error(
				responseData.message || "Failed to fetch jobs."
			);
			throw error;
		}

		return responseData;
	},
    async createJob(_: any, jobData: any) {
        let apiUrl = "http://localhost:3000/jobs";

        const response = await fetch(apiUrl, {
            method: "POST",
            body: JSON.stringify(jobData),
            headers: {
                "Content-Type": "application/json",
            },
        });

        const responseData = await response.json();

        if (!response.ok) {
            const error = new Error(
                responseData.message || "Failed to create job."
            );
            throw error;
        }

        return responseData;
    }
};
