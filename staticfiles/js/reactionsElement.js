document.addEventListener("DOMContentLoaded", function () {
  const reactionsElements = document.getElementsByClassName("reactionsEl");

  for (let reactionsElement of reactionsElements) {
    const reactionsId = reactionsElement.id;

    let reactionMap = {
      clap: 0,
      like: 0,
      heart: 0,
      trophy: 0,
    };

    let paragraphs = reactionsElement.getElementsByTagName("p");
    for (let p of paragraphs) {
      let reactionInt = parseInt(p.textContent);

      switch (reactionInt) {
        case 0:
          reactionMap["clap"] += 1;
          break;
        case 1:
          reactionMap["like"] += 1;
          break;
        case 2:
          reactionMap["heart"] += 1;
          break;
        case 3:
          reactionMap["trophy"] += 1;
          break;
      }
    }

    reactionsElement.innerHTML = `
        <div class="reaction-inner mx-2">
            <h6 class="reaction-emoji">👏
            <span class="reaction-badge"> <small>${reactionMap["clap"]}</small> </span>
            </h6>            
        </div>
        <div class="reaction-inner mx-2">
             <h6 class="reaction-emoji">👍
             <span class="reaction-badge" >${reactionMap["like"]}</span>
             </h6>            
        </div>
        <div class="reaction-inner mx-2">
             <h6 class="reaction-emoji">❤️
             <span class="reaction-badge"> ${reactionMap["heart"]}</span>
             </h6>            
        </div>
        <div class="reaction-inner mx-2">
             <h6 class="reaction-emoji">🏆
             <span class="reaction-badge"> ${reactionMap["trophy"]}</span>
             </h6>            
        </div>
    `;
  }
});
