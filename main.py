import streamlit as st
import random
import time

st.title("🍽️🎉 D.A.T.E. Game")
st.write("Welcome to the D.A.T.E. game! Fill in your dream options, roll the dice, and discover your perfect date night!")
st.write("Think of each part as a building block for your perfect date. Mix and match, customize, or let it spark new ideas. Whether it’s your first date or your fiftieth, this guide helps you create something memorable.")
# Function to eliminate options based on magic number
def mash_elimination(options, magic_number):
    index = 0
    while len(options) > 1:
        index = (index + magic_number - 1) % len(options)
        options.pop(index)
    return options[0]


# Input categories
st.header("Step 1: Enter Your Options")

st.subheader("🍽️ Dinner Options")
st.subheader("Each person selects a place to eat")
d1 = st.text_input("Dinner Option 1", "Sushi")
d2 = st.text_input("Dinner Option 2", "BBQ")
d3 = st.text_input("Dinner Option 3", "Italian")
d4 = st.text_input("Dinner Option 4", "Tacos")

st.subheader("🎯 Activity Options")
st.subheader("Each person selects an activity they would like to do")
a1 = st.text_input("Activity Option 1", "Mini Golf")
a2 = st.text_input("Activity Option 2", "Escape Room")
a3 = st.text_input("Activity Option 3", "Hiking")
a4 = st.text_input("Activity Option 4", "Painting Class")

st.subheader("🍦 Treat Options")
st.subheader("Each person selects a Treat they would like to eat")
t1 = st.text_input("Treat Option 1", "Ice Cream")
t2 = st.text_input("Treat Option 2", "Cupcakes")
t3 = st.text_input("Treat Option 3", "Milkshake")
t4 = st.text_input("Treat Option 4", "Churros")

st.subheader("✨ Ending Options")
st.subheader("Each person chooses how they want the date to wrap up")
e1 = st.text_input("Entertainment Option 1", "Slow Dancing")
e2 = st.text_input("Entertainment Option 2", "Stargazing")
e3 = st.text_input("Entertainment Option 3", "Evening Walk")
e4 = st.text_input("Entertainment Option 4", "Handshake")

# Roll the dice
st.header("Step 2: Roll the Magic Dice 🎲")
if st.button("Roll a 10-sided Die"):
    magic_number = random.randint(1, 10)
    st.success(f"You rolled a {magic_number}!")

    # Prepare lists
    dinner_list = [d1, d2, d3, d4]
    activity_list = [a1, a2, a3, a4]
    treat_list = [t1, t2, t3, t4]
    ending_list = [e1, e2, e3, e4]

    # Function to simulate and display global elimination
    def show_hybrid_elimination(title, dinner_list, activity_list, treat_list, ending_list, magic_number):
        st.subheader(f"{title} Hybrid Elimination Round")

        # Combine all options into one list with category tags
        temp_list = []
        for item in dinner_list:
            temp_list.append(("Dinner", item))
        for item in activity_list:
            temp_list.append(("Activity", item))
        for item in treat_list:
            temp_list.append(("Treat", item))
        for item in ending_list:
            temp_list.append(("Ending", item))

        # Track remaining items per category
        category_map = {
            "Dinner": dinner_list.copy(),
            "Activity": activity_list.copy(),
            "Treat": treat_list.copy(),
            "Ending": ending_list.copy()
        }

        locked_in = {}
        index = 0
        placeholder = st.empty()

        while len(temp_list) > 0:
            # Count forward magic_number steps
            for count in range(magic_number):
                current_index = (index + count) % len(temp_list)
                category, item = temp_list[current_index]
                placeholder.markdown(f"🔢 Counting: **{item}** ({category}) — {count + 1}")
                time.sleep(0.1)

            # Eliminate the item at the final count position
            index = (index + magic_number - 1) % len(temp_list)
            category, item = temp_list.pop(index)
            category_map[category].remove(item)
            placeholder.markdown(f"❌ Eliminated: **{item}** ({category})")
            time.sleep(1)

            # If only one item remains in a category, lock it in
            for cat in category_map:
                if cat not in locked_in and len(category_map[cat]) == 1:
                    locked_item = category_map[cat][0]
                    locked_in[cat] = locked_item
                    # Remove all remaining items of that category from temp_list
                    temp_list = [entry for entry in temp_list if entry[0] != cat]
                    placeholder.markdown(f"🔒 Locked in: **{locked_item}** ({cat})")
                    time.sleep(1)

            # Adjust index for next round
            if len(temp_list) > 0:
                index = index % len(temp_list)

        placeholder.empty()
        st.markdown("### 🏆 Final D.A.T.E. Night Selections:")
        for cat in ["Dinner", "Activity", "Treat", "Ending"]:
            st.markdown(f"✅ **{cat}:** {locked_in[cat]}")

        return locked_in


    # Run global elimination
    final_choices = show_hybrid_elimination(
        "Ultimate D.A.T.E. Decision",
        dinner_list,
        activity_list,
        treat_list,
        ending_list,
        magic_number
    )

    # Final result
    st.header("💖 Your D.A.T.E. Night Is...")
    st.markdown(f"**Dinner:** {final_choices['Dinner']}")
    st.markdown(f"**Activity:** {final_choices['Activity']}")
    st.markdown(f"**Treat:** {final_choices['Treat']}")
    st.markdown(f"**Ending:** {final_choices['Ending']}")

    st.balloons()
