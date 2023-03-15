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
}

getQuotes();
