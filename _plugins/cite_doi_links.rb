# frozen_string_literal: true

# Make {% cite %} links (e.g. in news items) point directly to the
# publication's DOI page, falling back to the in-page anchor for
# entries that don't have a DOI.
module Jekyll
  class Scholar
    module Utilities
      alias_method :anchor_link_target_for, :link_target_for

      def link_target_for(key)
        entry = bibliography[key]
        doi = entry && entry[:doi] && entry[:doi].to_s

        if doi && !doi.empty?
          "https://doi.org/#{doi}"
        else
          anchor_link_target_for(key)
        end
      end
    end
  end
end
