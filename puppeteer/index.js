import puppeteer from 'puppeteer';


const getQuotes = async () => {
	const browser = await puppeteer.launch({
		headless: false,
		defaultViewport: null,
	});

	const page = await browser.newPage();

	await page.goto('https://quotes.toscrape.com/', {
		waitUntil: 'domcontentloaded'
	});

	while(await page.$('.next a')) {
		const quotes = await page.evaluate(() => {
			const quoteList = document.querySelectorAll(".quote");
			return Array.from(quoteList).map((quote) => {
				const text = quote.querySelector('.text').innerText;
				const author = quote.querySelector('.author').innerText;
				return { text, author }
			})
		})
		console.log(quotes);
		await page.click('.next a');
		// await page.evaluate(() => {
		// 	document.querySelector('.next a').click();
		// })
	}

	await browser.close();
}

getQuotes();
