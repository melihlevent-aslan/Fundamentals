JavaScript (HTML/CSS): Live Coordinate Dashboard
This project trains DOM manipulation and event handling without relying on external libraries.

Step 1: HTML Skeleton: Create an index.html file. Define a main container div that will act as your "Map", an empty <ul id="coordinate-list"> for saved points, and a <button> to trigger the save action.

Step 2: CSS Layout: Write an inline or linked stylesheet. Give your Map div a fixed width, height, and a distinct background color or border so you know where the clickable area is. Use Flexbox to position the map next to the list.

Step 3: Event Tracking: In your JavaScript, select the Map div. Attach a mousemove event listener to it.

Step 4: Coordinate Extraction: Inside the event listener, extract the offsetX and offsetY properties from the event object. Update a text element on the screen to show these numbers changing live as you move the mouse.

Step 5: State Management: Create empty variables to hold the "current X" and "current Y". Update these variables inside your mousemove event.

Step 6: The Save Action: Attach a click event listener to your Save button. When clicked, read the current X and Y variables, create a new <li> element using template literals, and append it to your coordinate-list DOM element