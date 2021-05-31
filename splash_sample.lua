function main(splash, args)
  splash.private_mode_enabled = false
  headers = {
	  ['User-Agent'] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"
  }
  splash:set_custom_headers(headers)
  url = args.url
  assert(splash:go(url))
  assert(splash:wait(1))
  input_box = assert(splash:select("#search_form_input_homepage"))
 
  -- you can only write value in focus state
  input_box:focus()
  
  --send text
  input_box:send_text("my user agent")
  assert(splash:wait(1))

  -- select search button
  btn = assert(splash:select("#search_button_homepage"))
  btn:mouse_click()

  -- can also be done in one line
  input_box:send_keys("<Enter>")
  assert(splash:wait(2))

  -- selecting multiple elements in splash
  rur_tab = assert(splash:select_all(".filterPanelItem___2z5Gb"))
  rur_tab[5]:mouse_click()
  
  -- get the full page in png
  splash:set_viewport_full()

  -- creating object in lua
  return {
    image = splash:png(),
    html= splash:html()
  }
end
