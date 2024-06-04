document.addEventListener("DOMContentLoaded", function() {
    fetch('/chart-data')
        .then(response => response.json())
        .then(data => {
            console.log(data);

            // Define the PuBuGn color palette for all charts
            const puBuGnColors = [
                "#fff7fb", "#ece2f0", "#d0d1e6", "#a6bddb", 
                "#67a9cf", "#3690c0", "#02818a", "#016c59", 
                "#014636"
            ];

            // Tooltip div
            const tooltip = d3.select("body").append("div")
                .attr("class", "tooltip")
                .style("position", "absolute")
                .style("background", "#f9f9f9")
                .style("padding", "5px")
                .style("border", "1px solid #d3d3d3")
                .style("border-radius", "5px")
                .style("pointer-events", "none")
                .style("display", "none");

            // Function to show tooltip
            const showTooltip = (event, count, percentage, extraInfo) => {
                tooltip.transition().duration(200).style("display", "block");
                tooltip.html(`Count: ${count}<br>Percentage: ${percentage.toFixed(2)}%<br>${extraInfo}`)
                    .style("left", (event.pageX + 5) + "px")
                    .style("top", (event.pageY - 28) + "px");
            };

            // Function to hide tooltip
            const hideTooltip = () => {
                tooltip.transition().duration(500).style("display", "none");
            };

            // Calculate total counts
            const totalEducationCount = d3.sum(data.education.count);
            const totalOccupationCount = d3.sum(data.occupation.count);
            const totalHoursWorkedCount = data.hours_worked.data.length;

            // Horizontal Bar Chart for Education and Income Count
            const margin1 = { top: 25, right: 30, bottom: 40, left: 100 };
            const width1 = 700 - margin1.left - margin1.right;
            const height1 = 335 - margin1.top - margin1.bottom;

            const svg1 = d3.select("#chart1")
                .append("svg")
                .attr("width", width1 + margin1.left + margin1.right)
                .attr("height", height1 + margin1.top + margin1.bottom)
                .append("g")
                .attr("transform", `translate(${margin1.left},${margin1.top})`);

            const x1 = d3.scaleLinear()
                .domain([0, d3.max(data.education.count)])
                .range([0, width1]);

            const y1 = d3.scaleBand()
                .domain(data.education.labels)
                .range([0, height1])
                .padding(0.1);

            svg1.append("g")
                .selectAll("rect")
                .data(data.education.count)
                .enter()
                .append("rect")
                .attr("x", x1(0))
                .attr("y", (d, i) => y1(data.education.labels[i]))
                .attr("width", d => x1(d))
                .attr("height", y1.bandwidth())
                .attr("fill", (d, i) => puBuGnColors[i % puBuGnColors.length])
                .on("mouseover", function(event, d, i) {
                    const extraInfo = `Gender: ${data.education.gender[i]}<br>Race: ${data.education.race[i]}<br>Marital Status: ${data.education.marital_status[i]}`;
                    const percentage = (d / totalEducationCount) * 100;
                    showTooltip(event, d, percentage, extraInfo);
                })
                .on("mouseout", hideTooltip);

            svg1.append("g")
                .call(d3.axisLeft(y1));

            svg1.append("g")
                .attr("transform", `translate(0,${height1})`)
                .call(d3.axisBottom(x1));

            // Add titles
            svg1.append("text")
                .attr("x", width1 / 2)
                .attr("y", -10)
                .attr("text-anchor", "middle")
                .style("font-size", "16px")
                .text("Education Distribution");

            svg1.append("text")
                .attr("transform", `translate(${width1 / 2},${height1 + margin1.bottom - 10})`)
                .attr("text-anchor", "middle")
                .text("Count");

            svg1.append("text")
                .attr("transform", "rotate(-90)")
                .attr("x", -height1 / 2)
                .attr("y", -margin1.left + 20)
                .attr("text-anchor", "middle")
                .text("Education Level");

            // Horizontal Bar Chart for Occupation and Total Row Count (Chart3)
            const margin3 = { top: 25, right: 30, bottom: 40, left: 120 }; 
            const width3 = 700 - margin3.left - margin3.right;
            const height3 = 335 - margin3.top - margin3.bottom;

            const svg3 = d3.select("#chart3")
                .append("svg")
                .attr("width", width3 + margin3.left + margin3.right)
                .attr("height", height3 + margin3.top + margin3.bottom)
                .append("g")
                .attr("transform", `translate(${margin3.left},${margin3.top})`);

            const x3 = d3.scaleLinear()
                .domain([0, d3.max(data.occupation.count)])
                .range([0, width3]);

            const y3 = d3.scaleBand()
                .domain(data.occupation.labels)
                .range([0, height3])
                .padding(0.1);

            svg3.append("g")
                .selectAll("rect")
                .data(data.occupation.count)
                .enter()
                .append("rect")
                .attr("x", x3(0))
                .attr("y", (d, i) => y3(data.occupation.labels[i]))
                .attr("width", d => x3(d))
                .attr("height", y3.bandwidth())
                .attr("fill", (d, i) => puBuGnColors[i % puBuGnColors.length])
                .on("mouseover", function(event, d, i) {
                    const extraInfo = `Gender: ${data.occupation.gender[i]}<br>Race: ${data.occupation.race[i]}<br>Marital Status: ${data.occupation.marital_status[i]}`;
                    const percentage = (d / totalOccupationCount) * 100;
                    showTooltip(event, d, percentage, extraInfo);
                })
                .on("mouseout", hideTooltip);

            svg3.append("g")
                .call(d3.axisLeft(y3));

            svg3.append("g")
                .attr("transform", `translate(0,${height3})`)
                .call(d3.axisBottom(x3));

            // Add titles
            svg3.append("text")
                .attr("x", width3 / 2)
                .attr("y", -10)
                .attr("text-anchor", "middle")
                .style("font-size", "16px")
                .text("Occupation Distribution");

            svg3.append("text")
                .attr("transform", `translate(${width3 / 2},${height3 + margin3.bottom - 10})`)
                .attr("text-anchor", "middle")
                .text("Count");

            svg3.append("text")
                .attr("transform", "rotate(-90)")
                .attr("x", -height3 / 2)
                .attr("y", -margin3.left + 20)
                .attr("text-anchor", "middle")
                .text("Occupation");

            // Scatter Plot for Hours Worked and Age (Chart2)
            const margin2 = { top: 25, right: 30, bottom: 40, left: 100 };
            const width2 = 1350 - margin2.left - margin2.right;
            const height2 = 375 - margin2.top - margin2.bottom;

            const svg2 = d3.select("#chart2")
                .append("svg")
                .attr("width", width2 + margin2.left + margin2.right)
                .attr("height", height2 + margin2.top + margin2.bottom)
                .append("g")
                .attr("transform", `translate(${margin2.left},${margin2.top})`);

            const x2 = d3.scaleLinear()
                .domain([0, d3.max(data.hours_worked.data, d => d.x)])
                .range([0, width2]);

            const y2 = d3.scaleLinear()
                .domain([0, d3.max(data.hours_worked.data, d => d.y)])
                .range([height2, 0]);

            svg2.append("g")
                .selectAll("circle")
                .data(data.hours_worked.data)
                .enter()
                .append("circle")
                .attr("cx", d => x2(d.x))
                .attr("cy", d => y2(d.y))
                .attr("r", 5)
                .attr("fill", "rgba(112, 185, 176, 0.85)")
                .on("mouseover", function(event, d, i) {
                    const extraInfo = `Hours Worked: ${d.x}<br>Gender: ${data.hours_worked.gender[i]}<br>Race: ${data.hours_worked.race[i]}<br>Marital Status: ${data.hours_worked.marital_status[i]}`;
                    const percentage = (1 / totalHoursWorkedCount) * 100;
                    showTooltip(event, 1, percentage, extraInfo);
                })
                .on("mouseout", hideTooltip);

            svg2.append("g")
                .attr("transform", `translate(0,${height2})`)
                .call(d3.axisBottom(x2));

            svg2.append("g")
                .call(d3.axisLeft(y2));

            // Add titles
            svg2.append("text")
                .attr("x", width2 / 2)
                .attr("y", -10)
                .attr("text-anchor", "middle")
                .style("font-size", "16px")
                .text("Hours Worked vs Age");

            svg2.append("text")
                .attr("transform", `translate(${width2 / 2},${height2 + margin2.bottom - 10})`)
                .attr("text-anchor", "middle")
                .text("Hours Worked");

            svg2.append("text")
                .attr("transform", "rotate(-90)")
                .attr("x", -height2 / 2)
                .attr("y", -margin2.left + 20)
                .attr("text-anchor", "middle")
                .text("Age");
        })
        .catch(error => console.error('Error fetching chart data:', error));
});
